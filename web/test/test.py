import json
import requests

base_url = "http://ansible.office.bbobo.com"


def assign_task():
    data = {
        "action": "setup",
        "data": {"task_id": "123456abcdef",
                 "task_args": {"key": "value"},
                 "ips": "192.168.1.1,192.168.1.2,192.168.1.3"
                 }
    }

    data = {
        "action": "copy",
        "data": {"task_id": "123456abcdefge",
                 "task_args": {"filename": "test.json"},
                 "ips": "192.168.210.173"
                 }
    }

    req = requests.post("{0}/v1/task".format(base_url), json=data)
    print(req.json())


def get_task_result(task_id):
    req = requests.get("{0}/v1/task/{1}".format(base_url, task_id))
    print(req.json())


if __name__ == "__main__":
    assign_task()
    # get_task_result("123456abc")
