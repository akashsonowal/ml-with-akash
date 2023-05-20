from typing import Dict

import os
import numpy as np
import torch
from torch import nn
import urllib.request
import tarfile

from ml_foundations.models.deep_models.layers import GraphAttentionLayer

class CoraDataset:
  """
  content [
            ['31336' '0' '0' ... '0' '0' 'Neural_Networks'],
            ['1061127' '0' '0' ... '0' '0' 'Rule_Learning'], 
            ...
          ]
  citations [
              [35    1033]
              [35  103482]
              ...
            ]
  """
  labels: torch.Tensor
  classes: Dict[str, int]
  features: torch.Tensor
  adj_mat: torch.Tensor

  @staticmethod
  def _download():
    data_dir = './data/'
    if not os.path.exists(data_dir):
      os.makedirs(data_dir)
      url = 'https://linqs-data.soe.ucsc.edu/public/lbc/cora.tgz'
      filename = 'cora.tgz'
      urllib.request.urlretrieve(url, os.path.join(data_dir, filename))
      with tarfile.open(os.path.join(data_dir, filename), 'r:gz') as tar:
        tar.extractall(data_dir)
 
  def __init__(self, include_edges: bool = True):
    self.include_edges = include_edges
    self._download()
    content = np.genfromtxt('./data/cora/cora.content', dtype=np.dtype(str))
    citations = np.genfromtxt('./data/cora/cora.cites', dtype=np.int32)
    features = torch.Tensor(np.array(content[:, 1:-1], dtype=np.float32))
    self.features = features / features.sum(dim=1, keepdim=True)
    self.classes = {s: i for i, s in enumerate(set(content[:, -1]))}
    self.labels = torch.tensor([self.classes[i] for i in content[:, -1]], dtype=torch.long)
    paper_ids = np.array(content[:, 0], dtype=np.int32)
    ids_to_idx = {id_: i for i, id_ in enumerate(paper_ids)}
    self.adj_mat = torch.eye(len(self.labels), dtype=torch.bool)
    

class GAT():
  def __init__(self, in_features: int, n_hidden: int, n_classes: int, n_heads: int, dropout: float):
    super().__init__()
    self.layer1 = GraphAttentionLayer(in_features, n_hidden, n_heads, is_concat=True, dropout=dropout)
    self.activation = nn.ELU()
    self.output = GraphAttentionLayer(n_hidden, n_classes, 1, is_concat=True, dropout=dropout)
    self.dropout = nn.Dropout(dropout)

  def forward(self, x, adj_mat):
    x = self.dropout(x)
    x = self.layer1(x, adj_mat)
    x = self.activation(x)
    x = self.dropout(x)
    return self.output(x, adj_mat)

def main():
  pass

if __name__ == "__main__":
  main()
