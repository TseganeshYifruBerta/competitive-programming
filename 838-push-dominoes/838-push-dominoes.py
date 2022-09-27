class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes_list = list(dominoes)
        
        queue = collections.deque(
            [(idx, d) for idx, d in enumerate(dominoes_list) if d != "."]
        )

        while queue:
            cur_idx, cur_dominoe = queue.popleft()
            if cur_dominoe == "L" and cur_idx > 0 and dominoes_list[cur_idx - 1] == ".":
                queue.append((cur_idx - 1, "L"))
                dominoes_list[cur_idx - 1] = "L"

            elif (
                cur_dominoe == "R"
                and cur_idx + 1 < len(dominoes_list)
                and dominoes_list[cur_idx + 1] == "."
            ):
                if (
                    cur_idx + 2 < len(dominoes_list)
                    and dominoes_list[cur_idx + 2] == "L"
                ):
                    queue.popleft()

                else:
                    queue.append((cur_idx + 1, "R"))
                    dominoes_list[cur_idx + 1] = "R"

        return "".join(dominoes_list)