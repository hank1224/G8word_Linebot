from django.shortcuts import render

# Create your views here.
# 計畫採用前後端分離
# 使用者第一次呼叫就傳整頁面，之後按下按鈕就是透過js呼叫API要求資料，只更新資料頁面不刷新
# 關鍵字: Ajax, RESTful API, Django REST framework