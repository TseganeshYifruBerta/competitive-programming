class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        directories = defaultdict(list)
        for direc in range(len(paths)):
            files = paths[direc].split()
            
            for file in range(1, len(files)):
                f_name = files[file].split('(')
                
                directories[f_name[1]].append(files[0] + '/' + f_name[0])
        
     
                
        ans = []
        for file in directories:
            if len(directories[file]) > 1:
                ans.append(directories[file])
        return ans
                
        