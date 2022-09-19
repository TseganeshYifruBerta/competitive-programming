class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        directories = defaultdict(list)
        for direc in range(len(paths)):
            files = paths[direc].split()
            
            for file in range(1, len(files)):
                directories[files[0]].append(files[file])
        
        file_map = defaultdict(list)
        for directory in directories:
            files = directories[directory]
            for file in files:
                f = file.split('(')
                f_name = directory + '/' + f[0]
                file_map[f[1]].append(f_name)
                
        ans = []
        for file in file_map:
            if len(file_map[file]) > 1:
                ans.append(file_map[file])
        return ans
                
        