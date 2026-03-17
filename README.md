# GreaterWMS - 仓库管理系统 / Warehouse Management System

## 简介 / Introduction

GreaterWMS 是一个基于 Django REST Framework 构建的开源仓库管理系统（WMS），提供完整的进销存管理功能。

GreaterWMS is an open-source Warehouse Management System (WMS) built with Django REST Framework, providing comprehensive inventory management capabilities.

## 功能模块 / Features

| 模块 | 说明 | Module | Description |
|------|------|--------|-------------|
| 商品管理 | 商品信息的增删改查 | Goods | CRUD for product catalog |
| 供应商管理 | 供应商信息管理 | Supplier | Supplier information management |
| 客户管理 | 客户信息管理 | Customer | Customer information management |
| 库存管理 | 实时库存查询 | Stock | Real-time inventory tracking |
| 入库管理 | ASN单据管理 | Inbound | ASN (Advance Shipping Notice) management |
| 出库管理 | DN单据管理 | Outbound | DN (Delivery Note) management |
| 员工管理 | 仓库员工信息 | Staff | Warehouse staff management |

## 技术栈 / Tech Stack

- **Python** 3.12+
- **Django** 5.x / 6.x
- **Django REST Framework** 3.14+
- **djangorestframework-simplejwt** — JWT authentication
- **django-filter** — Advanced filtering
- **django-cors-headers** — CORS support
- **SQLite** (default) / PostgreSQL / MySQL

## 快速开始 / Quick Start

### 安装依赖 / Install Dependencies

```bash
pip install -r requirements.txt
```

### 数据库迁移 / Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### 创建超级用户 / Create Superuser

```bash
python manage.py createsuperuser
```

### 启动服务 / Run Server

```bash
python manage.py runserver
```

### Docker

```bash
docker-compose up --build
```

## API 接口 / API Endpoints

### 认证 / Authentication

```
POST /api/token/          # 获取 JWT token / Obtain JWT token
POST /api/token/refresh/  # 刷新 token / Refresh token
```

### 主要接口 / Main Endpoints

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/goods/goods/` | GET/POST/PUT/DELETE | 商品管理 |
| `/api/supplier/supplier/` | GET/POST/PUT/DELETE | 供应商管理 |
| `/api/customer/customer/` | GET/POST/PUT/DELETE | 客户管理 |
| `/api/stock/stock/` | GET/POST/PUT/DELETE | 库存管理 |
| `/api/inbound/asnlist/` | GET/POST/PUT/DELETE | ASN单管理 |
| `/api/inbound/asndetail/` | GET/POST/PUT/DELETE | ASN明细管理 |
| `/api/outbound/dnlist/` | GET/POST/PUT/DELETE | DN单管理 |
| `/api/outbound/dndetail/` | GET/POST/PUT/DELETE | DN明细管理 |
| `/api/staff/staff/` | GET/POST/PUT/DELETE | 员工管理 |

### 请求示例 / Request Example

```bash
# 获取 token / Get token
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "password"}'

# 查询商品列表 / List goods
curl -X GET http://localhost:8000/api/goods/goods/ \
  -H "Authorization: Bearer <access_token>"
```

## 运行测试 / Run Tests

```bash
python manage.py test
```

## 项目结构 / Project Structure

```
GreaterWMS/
├── wms/                  # 项目配置 / Project config
│   ├── settings.py
│   └── urls.py
├── goods/                # 商品管理
├── supplier/             # 供应商管理
├── customer/             # 客户管理
├── stock/                # 库存管理
├── inbound/              # 入库管理
├── outbound/             # 出库管理
├── staff/                # 员工管理
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── manage.py
```

## 许可证 / License

MIT License