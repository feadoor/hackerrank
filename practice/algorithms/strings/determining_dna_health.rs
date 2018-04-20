use std::collections::VecDeque;
use std::iter::FromIterator;
use std::io::{self, BufRead};

const ALPHABET_SIZE: usize = 26;

struct Gene<'a> {
    pub word: &'a str,
    pub weight: usize,
}

impl<'a> Gene<'a> {
     pub fn new(word: &'a str, weight: usize) -> Gene {
        Gene {
            word: word,
            weight: weight,
        }
     }
}

struct Node {
    pub fallback_idx: usize,
    pub children_idx: Vec<usize>,
    pub weight: usize,
}

impl Node {

    pub fn new() -> Node {
        Node {
            fallback_idx: 0,
            children_idx: vec![0; ALPHABET_SIZE],
            weight: 0,
        }
    }
}

struct AhoCorasick {
    nodes: Vec<Node>,
}

impl AhoCorasick {

    pub fn new(genes: &[Gene]) -> AhoCorasick {
        let mut ac = AhoCorasick { nodes: vec![Node::new()] };
        ac.build_trie(genes);
        ac.build_fsa();
        ac
    }

    pub fn match_weight(&self, text: &str) -> usize {
        let mut node_idx = 0;
        let mut total_weight = 0;
        for byte in text.bytes() {
            while node_idx != 0 && !self.has_child(node_idx, byte) {
                node_idx = self.fallback(node_idx);
            }
            node_idx = self.next_node(node_idx, byte);
            total_weight += self.weight(node_idx);
        }
        total_weight
    }

    fn build_trie(&mut self, genes: &[Gene]) {
        for gene in genes {
            let mut current_node = 0;
            for byte in gene.word.bytes() {
                current_node = self.next_node_or_create(current_node, byte);
            }
            self.nodes[current_node].weight += gene.weight;
        }
    }

    fn build_fsa(&mut self) {
        let mut queue = VecDeque::from_iter((0..ALPHABET_SIZE)
            .map(|x| self.nodes[0].children_idx[x])
            .filter(|&x| x != 0)
        );
        while !queue.is_empty() {
            let node_idx = queue.pop_front().unwrap();
            for byte in b'a'..(b'a' + ALPHABET_SIZE as u8) {
                if self.has_child(node_idx, byte) {
                    let mut fallback_idx = self.fallback(node_idx);
                    while fallback_idx != 0 && !self.has_child(fallback_idx, byte) {
                        fallback_idx = self.fallback(fallback_idx);
                    }
                    let next_node_idx = self.next_node(node_idx, byte);
                    self.nodes[next_node_idx].fallback_idx = self.next_node(fallback_idx, byte);
                    self.nodes[next_node_idx].weight += self.nodes[self.fallback(next_node_idx)].weight;
                    queue.push_back(next_node_idx);
                }
            }
        }
    }

    fn fallback(&self, node_idx: usize) -> usize {
        self.nodes[node_idx].fallback_idx
    }

    fn weight(&self, node_idx: usize) -> usize {
        self.nodes[node_idx].weight
    }

    fn next_node(&self, current_node: usize, byte: u8) -> usize {
        self.nodes[current_node].children_idx[(byte - b'a') as usize]
    }

    fn has_child(&self, current_node: usize, byte: u8) -> bool {
        self.next_node(current_node, byte) != 0
    }

    fn next_node_or_create(&mut self, current_node: usize, byte: u8) -> usize {
        match self.next_node(current_node, byte) {
            0 => {
                self.nodes.push(Node::new());
                let added_idx = self.nodes.len() - 1;
                self.nodes[current_node].children_idx[(byte - b'a') as usize] = added_idx;
                added_idx
            },
            idx => idx,
        }
    }
}

struct IncrementalAhoCorasick<'a> {
    ahos: Vec<AhoCorasick>,
    sizes: Vec<usize>,
    genes: Vec<Gene<'a>>,
}

impl<'a> IncrementalAhoCorasick<'a> {

    pub fn new() -> IncrementalAhoCorasick<'a> {
        IncrementalAhoCorasick {
            ahos: Vec::new(),
            sizes: Vec::new(),
            genes: Vec::new(),
        }
    }

    pub fn insert(&mut self, gene: Gene<'a>) {
        self.genes.push(gene);
        self.sizes.push(1);

        while self.sizes.len() > 1 && self.sizes[self.sizes.len() - 1] == self.sizes[self.sizes.len() - 2] {
            self.ahos.pop();
            let size = self.sizes.pop().unwrap();
            let len  = self.sizes.len();
            self.sizes[len - 1] += size;
        }

        let num_genes = self.genes.len();
        let size = self.sizes.last().unwrap();
        self.ahos.push(AhoCorasick::new(&self.genes[num_genes - size..num_genes]));
    }

    pub fn match_weight(&self, text: &str) -> usize {
        self.ahos.iter().map(|aho| aho.match_weight(text)).sum()
    }
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let num_genes: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let words: Vec<_> = lines.next().unwrap().unwrap().trim().split_whitespace().map(|x| x.to_string()).collect();
    let weights: Vec<usize> = lines.next().unwrap().unwrap().trim().split_whitespace().map(|x| x.parse().unwrap()).collect();

    let num_strands: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let mut lefts: Vec<Vec<usize>> = vec![vec![]; num_genes];
    let mut rights: Vec<Vec<usize>> = vec![vec![]; num_genes];
    let mut strands = vec![];
    let mut healths = vec![0; num_strands];
    for strand_idx in 0..num_strands {
        let next_line: Vec<_> = lines.next().unwrap().unwrap().trim().split_whitespace().map(|x| x.to_string()).collect();
        lefts[next_line[0].parse::<usize>().unwrap()].push(strand_idx);
        rights[next_line[1].parse::<usize>().unwrap()].push(strand_idx);
        strands.push(next_line[2].to_string());
    }

    let mut incremental_aho_corasick = IncrementalAhoCorasick::new();
    for (gene_idx, (word, weight)) in words.iter().zip(weights.iter()).enumerate() {
        for &strand_idx in &lefts[gene_idx] {
            healths[strand_idx] -= incremental_aho_corasick.match_weight(&strands[strand_idx]);
        }
        incremental_aho_corasick.insert(Gene::new(word, *weight));
        for &strand_idx in &rights[gene_idx] {
            healths[strand_idx] += incremental_aho_corasick.match_weight(&strands[strand_idx]);
        }
    }

    println!("{} {}", healths.iter().min().unwrap(), healths.iter().max().unwrap());
}
