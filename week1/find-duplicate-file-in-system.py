class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
            
        content_dict = {}

        for path in paths:
            path_info = path.split(" ")
            directory = path_info[0]
            files_info = path_info[1:]

            for file_info in files_info:
                file_parts = file_info.split("(")
                file_name = file_parts[0]
                file_content = file_parts[1][:-1]

                full_path = f"{directory}/{file_name}"

                if file_content in content_dict:
                    content_dict[file_content].append(full_path)
                else:
                    content_dict[file_content] = [full_path]

        duplicate_groups = [group for group in content_dict.values() if len(group) > 1]

        return duplicate_groups

