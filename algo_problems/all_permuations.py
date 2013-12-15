#/usr/local/bin/python
class Permuation(object):
  def __init__(self, input_list):
    self._input = input_list
    self._permuations = []
  def perm(self, s_idx=None, e_idx=None):
    if s_idx is None:
        s_idx = 0
    if e_idx is None:
        e_idx = len(self._input) - 1
    
    if s_idx == e_idx:
      self._permuations.append(tuple(self._input))  
    for idx in range(s_idx, e_idx + 1):
      self._input[s_idx], self._input[idx] = self._input[idx], self._input[s_idx]
      self.perm(s_idx + 1, e_idx)
      self._input[idx], self._input[s_idx] = self._input[s_idx], self._input[idx]

perm = Permuation([1,2,3])
perm.perm()
for i in perm._permuations:
    print i
