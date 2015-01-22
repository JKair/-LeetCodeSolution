class Solution:   
  # @param s, a string    
  # @return an integer    
  def lengthOfLastWord(self, s):        
    token = s.split(' ')        
    result = [""]        
    for x in xrange(len(token)):            
      if token[x] != "":                
        result.append(token[x])       
    return len(result[-1])