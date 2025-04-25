# Kafka to MongoDB Data Pipeline
**Người thực hiện:**  


**Ngày cập nhật:**  
2025/04/25

---

## 1. Vai trò của `config.ini`

- **Chứa thông tin cấu hình** cho cả Kafka và MongoDB:
  - Địa chỉ, thông tin xác thực Kafka (bootstrap servers, security, user, password, topic,...)
  - Thông tin kết nối MongoDB (uri, database, collection)
- Giúp script có thể **dễ dàng cấu hình lại** khi thay đổi môi trường hoặc server.

---

## 2. Tóm tắt các phần chính của chương trình

### **A. Đọc dữ liệu từ Kafka**

- Đọc các tham số cấu hình Kafka từ file `config.ini`.
- Kết nối tới Kafka server, lắng nghe một topic nhất định.
- Nhận các message (dữ liệu sự kiện, hành vi người dùng, v.v.) từ Kafka.

### **B. Ghi dữ liệu vào MongoDB**

- Đọc cấu hình kết nối MongoDB từ file `config.ini`.
- Kết nối tới MongoDB, xác định database và collection sẽ lưu dữ liệu.
- Với mỗi message nhận được từ Kafka:
  - Cố gắng parse thành JSON, nếu lỗi sẽ lưu dưới dạng raw string.
  - Ghi dữ liệu vào MongoDB collection đã chỉ định.

---

## 3. Ví dụ về 1 document trong MongoDB

Một document ngẫu nghiên  sẽ có cấu trúc như sau:

```json
{
  "_id": "5e84b70173c8be36d007741e",
  "time_stamp": 1744667539,
  "ip": "2.136.107.233",
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15",
  "resolution": "1024x1366",
  "user_id_db": "480201",
  "device_id": "7b3ecf99-928b-4569-887b-9531824424d2",
  "api_version": "1.0",
  "store_id": "8",
  "local_time": "2025-04-15 04:52:19",
  "show_recommendation": "true",
  "current_url": "https://www.glamira.es/county/recommendation/list/id/108697/alloy/yellow-750/diamond/rhodolite-cabochon/price/353.00",
  "referrer_url": "https://www.glamira.es/glamira-pendant-yogine.html?itm_source=recommendation&itm_medium=detail&diamond=rhodolite-cabochon&alloy=yellow-750",
  "email_address": "",
  "collection": "view_all_recommend",
  "product_id": "108697",
  "option": {
    "alloy": "yellow-750",
    "stone": "8",
    "pearlcolor": "",
    "finish": "",
    "price": "353.00",
    "category id": "757",
    "Kollektion": "",
    "kollektion_id": ""
  },
  "id": "31e2a2b7-0e17-4e10-995b-4fd49e638b75"
}
```

---

## 4. Thống kê dữ liệu

- Số lượng document đã lưu trong collection `product_views`:
  - **207,191** documents  
    *(Kiểm tra bằng lệnh: `db.product_views.countDocuments()` trong MongoDB)*

---

## 5. Đánh giá chung

- Pipeline thực hiện tốt việc chuyển dữ liệu từ Kafka sang MongoDB.
- Cấu hình linh hoạt, dễ thay đổi.
- Dữ liệu được ghi nhận liên tục, số lượng lớn.
- Nếu message không phải JSON hợp lệ, vẫn không bị mất dữ liệu (được lưu dạng raw text).
- Có thể mở rộng thêm kiểm soát trùng lặp hoặc cập nhật document nếu cần thiết.

---


[Điền ngày]
