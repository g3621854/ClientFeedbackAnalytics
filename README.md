## 專案簡介
本專案是一個客訴網站，提供查看各店在Google地圖上的評論分數及評論內容，並整理為關鍵字，方便用戶查看每家店的關鍵字以及評論內容。

## 功能介紹
- 查看各店的Google地圖評論分數
- 查看各店的Google地圖評論內容
- 將評論內容整理為關鍵字，便於查看和覆盤檢討

## 安裝指南
### 前提條件
- Python 3.12
- Django 5.0

### 步驟
1. 克隆此專案: `git clone https://github.com/g3621854/ClientFeedbackAnalytics.git`
2. 進入專案目錄: `cd yourrepository`
3. 安裝依賴: `pip install -r requirements.txt`
4. 進行遷移: `python manage.py migrate`
5. 啟動伺服器: `python manage.py runserver`

## 使用說明
- 啟動伺服器: `python manage.py runserver`
- 訪問網站: 在瀏覽器中打開 `http://127.0.0.1:8000/googlemap_reviews/`
- 查看評論及關鍵字: 在主頁面點選店名或日期進行查詢

## 文件結構
- `models.py`: 定義數據模型
- `views_api.py`: 處理API請求和返回JSON格式的視圖函數
- `views_web.py`: 處理Web請求和返回HTML頁面的視圖函數
- `templates/`: 存放HTML模板文件

## 附加資源
- [操作畫面]
  ![image](https://github.com/g3621854/ClientFeedbackAnalytics/blob/main/googlemap_reviews/resources/Django_web_template.gif)

- [網站連結](https://honestcoe.zeabur.app/googlemap_reviews/)
