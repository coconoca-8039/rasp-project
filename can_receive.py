import subprocess
import threading
import queue
import posix_ipc
import sys

# CANデータの読み取りを行うスレッドの関数
def read_can_data(q):
    cmd = ["candump", "can0", "-x"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    for line in process.stdout:
        q.put(line.decode().strip())  # キューにデータを追加

def can_receive():
    # CANインターフェースの設定
    # 既に can0 が設定されている場合は、以下のコマンドは不要かもしれません
    subprocess.run(["sudo", "ip", "link", "set", "can0", "type", "can", "bitrate", "500000"])
    subprocess.run(["sudo", "ip", "link", "set", "can0", "up"])

    # データを格納するキュー
    data_queue = queue.Queue()

    # スレッドの作成と処理の開始
    read_thread = threading.Thread(target=read_can_data, args=(data_queue,))
    read_thread.start()

    # POSIX IPC メッセージキューの設定
    mq_name = "/can_data_mq"
    try:
        mq = posix_ipc.MessageQueue(mq_name, posix_ipc.O_CREAT)
    except posix_ipc.ExistentialError:
        print(f"Unable to open or create the message queue '{mq_name}'. Exiting.")
        sys.exit(1)

    # リストから不要な要素を消す
    exclude_indices = [1, 3, 4, 5, 7, 8, 10]

    while True:
        if not data_queue.empty():
            data = data_queue.get().split(' ')  # キューからデータを取得し、スペースで分割
            filtered_data = [elem for i, elem in enumerate(data) if i not in exclude_indices]
            print(filtered_data)  # 分割されたデータのリストを出力

            # メッセージキューを使用してデータを送信
            try:
                mq.send(' '.join(filtered_data).encode())
            except posix_ipc.ExistentialError:
                print(f"Unable to send data to the message queue '{mq_name}'.")
            except posix_ipc.BusyError:
                print("Message queue is full, skipping this message.")

    # メッセージキューを閉じる
    mq.close()
    mq.unlink()

if __name__ == "__main__":
    can_receive()