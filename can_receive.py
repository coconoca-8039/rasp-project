import subprocess
import threading
import queue

# CANデータの読み取りを行うスレッドの関数
def read_can_data(q):
    cmd = ["candump", "can0", "-x"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    for line in process.stdout:
        q.put(line.decode().strip())  # キューにデータを追加

def can_receive():
    # CANインターフェースの設定
    subprocess.run(["sudo", "ip", "link", "set", "can0", "type", "can", "bitrate", "500000"])
    subprocess.run(["sudo", "ip", "link", "set", "can0", "up"])

    # データを格納するキュー
    data_queue = queue.Queue()

    # スレッドの作成と処理の開始
    read_thread = threading.Thread(target=read_can_data, args=(data_queue,))
    read_thread.start()

    # リストから不要な要素を消す
    exclude_indics = [1, 3, 4, 5, 7, 8, 10]

    while True:
        if not data_queue.empty():
            data = data_queue.get().split(' ')  # キューからデータを取得し、スペースで分割
            filtered_data = [elem for i, elem in enumerate(data) if i not in exclude_indics]
            print(filtered_data)  # 分割されたデータのリストを出力

if __name__ == "__main__":
    can_receive()