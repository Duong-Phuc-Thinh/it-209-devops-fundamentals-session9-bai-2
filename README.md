# Bài 2: Khởi chạy Web Server Nginx với Port Mapping

## Mục tiêu
Khởi chạy một Nginx Web Server dưới dạng container ở chế độ ngầm (`-d`), thực hiện ánh xạ cổng mạng (`-p 8080:80`) và dọn dẹp container sau khi kiểm tra xong.

## Bối cảnh & Ràng buộc
- Sử dụng image nhẹ: `nginx:alpine`
- Tên container: `my-web`
- Ánh xạ cổng: `8080:80` (Cổng 8080 trên host -> Cổng 80 trong container)
- Kiểm tra phản hồi HTTP có chứa chuỗi `"Welcome to nginx!"`.
- Dừng và xóa container sau khi hoàn thành.

## Hướng dẫn chạy

### Cách 1: Sử dụng Python Script
Chạy file `main.py` để tự động hóa toàn bộ quá trình:
```bash
python main.py
```

### Cách 2: Chạy trực tiếp qua Docker CLI
1. Khởi chạy container:
```bash
docker run -d -p 8080:80 --name my-web nginx:alpine
```

2. Kiểm tra trang web bằng `curl`:
```bash
curl http://localhost:8080
```

3. Dọn dẹp container:
```bash
docker stop my-web && docker rm my-web
```