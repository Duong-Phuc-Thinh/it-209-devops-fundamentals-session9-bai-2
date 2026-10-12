import subprocess
import time
import urllib.request

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def main():
    print("1. Khởi chạy Nginx container...")
    code, out, err = run_cmd("docker run -d -p 8080:80 --name my-web nginx:alpine")
    if code != 0:
        print(f"Lỗi khi chạy container: {err.strip()}")
        return
    
    print(f"Container ID: {out.strip()}")
    time.sleep(2)
    
    print("\n2. Kiểm tra trang web...")
    try:
        with urllib.request.urlopen("http://localhost:8080") as response:
            html = response.read().decode('utf-8')
            if "Welcome to nginx!" in html:
                print("[SUCCESS] Phản hồi từ server thành công! Tìm thấy 'Welcome to nginx!'.")
            else:
                print("[FAILED] Không tìm thấy 'Welcome to nginx!' trong phản hồi.")
    except Exception as e:
        print(f"[ERROR] Lỗi truy vấn HTTP: {e}")
    
    print("\n3. Dọn dẹp container...")
    code, out, err = run_cmd("docker stop my-web && docker rm my-web")
    if code == 0:
        print("Đã dọn dẹp container my-web thành công.")
    else:
        print(f"Lỗi khi dọn dẹp: {err.strip()}")

if __name__ == "__main__":
    main()