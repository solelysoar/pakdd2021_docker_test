import json
from ai_hub import inferServer
# import logging
# log = logging.getLogger("werkzeug")
# log.setLevel(logging.ERROR)


class MyInfer(inferServer):
    def __init__(self, model):
        super().__init__(model)

    # 数据前处理
    def pre_process(self, request):
        json_data = json.loads(request.get_data().decode('utf-8'))
        return json_data

    def predict(self, data):
        return data

    # 数据后处理
    def post_process(self, data):
        res = []
        if isinstance(data, dict):
            # if 'mce_log' in data:
            #     mce_data = data['mce_log']
            #     if isinstance(mce_data, list):
            #         for item in mce_data:
            #             res.append({'serial_number': item[0], 'pti': 0})
            # if 'address_log' in data:
            #     address_data = data['address_log']
            #     if isinstance(address_data, list):
            #         for item in address_data:
            #             res.append({'serial_number': item[0], 'pti': 0})
            if 'kernel_log' in data:
                kernel_data = data['kernel_log']
                if isinstance(kernel_data, list):
                    for item in kernel_data:
                        res.append({'serial_number': item[-3], 'pti': 5})
            print(json.dumps(res))
        return json.dumps(res)


if __name__ == "__main__":
    my_infer = MyInfer(None)
    my_infer.run(debuge=True)
