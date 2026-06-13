# FizzBuzz API (FastAPI)

This project implements a configurable FizzBuzz REST API using FastAPI.

---

## 🚀 Features

- REST API endpoint for FizzBuzz logic
- Configurable parameters via query string
- Health check endpoint
- Input validation
- Unit and integration tests
- Dockerized application
- Logging support

---

## 📌 Problem Statement

Given:
- int1, int2 (divisors)
- limit (upper bound)
- str1, str2 (replacement strings)

Return numbers from 1 to `limit` with rules:
- multiples of int1 → str1
- multiples of int2 → str2
- multiples of both → str1 + str2
- otherwise → number

---

## 📡 API Endpoints

### 🔹 1. FizzBuzz Endpoint

**URL:**
