import os
import re
import psutil


current_dir = os.getcwd()


def is_process_running(pid):
    try:
        process = psutil.Process(int(pid))
        return process.is_running()
    except (psutil.NoSuchProcess, ValueError):
        return False


def nodes_status(node_dirs) -> dict:
    """
    This function will return a tuple of dicts where innner dicts will have 4 items (node_dir_path, node_cli_path, pid_text_path and state of node)
    state of node => 1 means running and 0 means not running
    """
    node_stat = ()
    for each_dir in node_dirs:
        for root, dirs, files in os.walk(each_dir):
            if 'node_cli.py' in files or "pid.txt" in files:
                node_cli_path = os.path.join(root, 'node_cli.py')
                pid_txt_path = os.path.join(root, 'pid.txt')
                node_stat += ({
                    "node_dir_path": each_dir,
                    "node_cli_path": node_cli_path,
                    "pid_text_path": pid_txt_path
                },)

    pass


def nodes_running(node_dir) -> int:
    """This function will return the """
    pass


def zeuz_node_dirs(base_dir, node_dir_pattern):
    """
    This function will return the path of zeuz nodes that starts with `node_`
    """
    all_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    filtered_dirs = [d for d in all_dirs if re.match(node_dir_pattern, d)]
    directory_paths = [os.path.join(base_dir, d) for d in filtered_dirs]
    return tuple(directory_paths)


if __name__ == "__main__":
    # Todo: Get the requested number of nodes
    req_number_of_nodes = 1
    # Todo: Get the server address and api to run the nodes
    server_address = "server_address"
    api_key = "api_key"

    # Todo: Store the server_address, api_key, req_number_of_nodes in a config file

    node_dir_name_pattern = r"^node_\d+$"
    zeuz_nodes = zeuz_node_dirs(current_dir, node_dir_name_pattern)
    number_of_zeuz_node_dirs = len(zeuz_nodes)

    # Step 1: req number of node folder exists or node
    if number_of_zeuz_node_dirs == 0:
        # Todo: clone from git
        print("No such node directory found")
    elif number_of_zeuz_node_dirs >= req_number_of_nodes:
        print("Required number of node folders have been found!")
        # Todo: check if the existing node requires an update from git
    elif number_of_zeuz_node_dirs <= req_number_of_nodes:
        print(f"Required Nodes: {req_number_of_nodes}\tFound nodes: {len(zeuz_nodes)}")
        # Todo:create the rest
        # Todo: check if the existing node requires an update from git

    all_nodes_status = nodes_status(zeuz_nodes)
    number_of_running_nodes = sum(1 for item in all_nodes_status if item["status"] == 0)

    if number_of_running_nodes == req_number_of_nodes:
        print("Required number of nodes are running. No action require")
    elif number_of_running_nodes >= req_number_of_nodes:
        print(f"Extra {number_of_running_nodes-req_number_of_nodes} running on the background")
    elif number_of_running_nodes <= req_number_of_nodes:
        # Todo: Find out which node is not running and run it or those
        pass

    # Todo:
    pass
