import socket
import threading
import pickle
import os

def handle_client(conn):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # ファイルの存在と内容を確認
            if os.path.exists('can_data.pkl') and os.path.getsize('can_data.pkl') > 0:
                try:
                    with open('can_data.pkl', 'rb') as file:
                        can_data = pickle.load(file)
                        print(can_data)
                    # ファイルの内容をクリア
                    open('can_data.pkl', 'wb').close()
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Pickle file not found or is empty.")
                
            # pickleファイルからデータを読み込む
            try:
                with open('can_data.pkl', 'rb') as file:
                    can_data = pickle.load(file)
                    print(can_data)  # pickleファイルの内容を表示
                # pickleファイルの内容をクリア
                open('can_data.pkl', 'wb').close()
            except FileNotFoundError:
                print("Pickle file not found.")
            except Exception as e:
                print(f"An error occurred: {e}")

def main_visual_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12345))
        s.listen()
        while True:
            conn, _ = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn,))
            client_thread.start()

if __name__ == "__main__":
    main_visual_server()