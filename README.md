# 🦾 GO2 Isaac Lab Suite

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Build and Test](https://github.com/Nersisiian/go2-isaac-lab-suite/actions/workflows/build.yml/badge.svg)](https://github.com/Nersisiian/go2-isaac-lab-suite/actions/workflows/build.yml)
[![Check Links](https://github.com/Nersisiian/go2-isaac-lab-suite/actions/workflows/check-links.yml/badge.svg)](https://github.com/Nersisiian/go2-isaac-lab-suite/actions/workflows/check-links.yml)

**Продвинутая система для разработки и обучения AI-агентов для четвероногого робота Go2**  
на базе NVIDIA Isaac Lab (GPU-ускоренная физика, массово-параллельное RL).

## 🎯 Для кого

- 🤖 **Robotics engineers** – отработка алгоритмов управления в симуляции  
- 🧠 **ML / RL engineers** – масштабируемое обучение с подкреплением  
- 🔬 **Research проекты** – бенчмаркинг, доменная рандомизация  
- 🚀 **Стартап в AI + Robotics** – быстрый прототип Sim2Real  

## 🔥 Особенности

- 🐕 **Четвероногий робот Go2** (12 DOF, IMU, контактные сенсоры)  
- ⚙️ **Низкоуровневый контроль суставов** (PD, позиция, усилие)  
- 🧠 **Среды, готовые для RL** (награды, наблюдения, команды)  
- 🎯 **Интеграция сенсоров** (IMU, состояние, опциональный LiDAR)  
- 🚀 **Физика с ускорением на GPU** (тысячи параллельных симуляций)  
- 🧪 **Архитектура исследовательского уровня** (модульные конфиги, Hydra)  
- ✅ **CI/CD на GitHub Actions** (линтер, проверка ссылок, тесты импортов)  

## 🏗️ Структура проекта
```
go2-isaac-lab-suite/
├── .github/workflows/ # CI/CD (build, check-links)
├── configs/ # Hydra конфиги (задачи, алгоритмы)
├── go2_extreme/ # Основной код
│ ├── robots/ # Определение роботов (Go2, с манипулятором)
│ ├── tasks/ # Сценарии: ходьба, прыжки, кувырок, манипуляция
│ ├── rewards/ # Кастомные функции награды
│ └── utils/ # Вспомогательные функции
├── policies/ # Сохранённые модели (.pt)
├── scripts/ # Скрипты установки и загрузки моделей
├── train.py # Запуск обучения
├── play.py # Визуализация обученной политики
├── evaluate.py # Оценка модели на эпизодах
├── Dockerfile # Воспроизводимый контейнер
├── requirements.txt # Python зависимости (для CI, без Isaac Lab)
└── README.md

```
## ⚡ Tech Stack

- Python 3.10+  
- **NVIDIA Isaac Lab** (основной фреймворк)  
- Isaac Sim / PhysX (GPU-физика)  
- PyTorch, Hydra, Omegaconf  
- Reinforcement Learning (PPO, SAC – через RSL-RL)  
- ROS2 (опционально, для Sim2Real)  
- CUDA / GPU (обязательно для обучения)  

## 🚀 Установка

### Требования
- NVIDIA GPU с **8+ ГБ VRAM** (RTX 3060 или лучше)  
- **CUDA 11.8+** и драйверы  
- **Docker** (рекомендуется) или чистая Ubuntu 20.04/22.04  

### Быстрый старт (локально)

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/Nersisiian/go2-isaac-lab-suite.git
cd go2-isaac-lab-suite

# 2. Создайте conda окружение
conda create -n go2 python=3.10 -y
conda activate go2

# 3. Установите зависимости (без Isaac Lab — он ставится отдельно)
pip install -r requirements.txt

# 4. Установите сам проект в режиме разработки
pip install -e .
```
Установка Isaac Lab (обязательно для обучения)
Следуйте официальной инструкции NVIDIA:
Isaac Lab Installation Guide

Кратко:
```
# Скачайте Isaac Sim через Omniverse Launcher или используйте Docker
docker pull nvcr.io/nvidia/isaac-sim:2024.1.0
# Или клонируйте репозиторий Isaac Lab
git clone https://github.com/isaac-sim/IsaacLab.git
cd IsaacLab
./isaaclab.sh --install

```
После установки Isaac Lab не забудьте связать расширение:
```
# Из корня IsaacLab
./isaaclab.sh -p -m pip install -e /path/to/go2-isaac-lab-suite
```
▶️ Использование
Запуск обучения
```
# Ходьба по ровной поверхности
python train.py --task go2_walk

# Бег с целевой скоростью 2 м/с
python train.py --task go2_run --config configs/task/run.yaml

# Прыжки через препятствие
python train.py --task go2_jump

# Кувырок назад (backflip)
python train.py --task go2_backflip --num_envs 4096

# Манипуляция с arm (если добавлен)
python train.py --task go2_manipulate
```
Визуализация обученной политики
```
python play.py --checkpoint policies/go2_walk_final.pt --rendering
```
Оценка производительности
```
python evaluate.py --checkpoint policies/go2_walk_final.pt --num_episodes 100

```
🧪 Задачи (Tasks)
```
Задача	Описание	Статус
🐾 Locomotion	Ходьба, бег с переменной скоростью	✅ Реализовано
🧍 Balance	Удержание равновесия на нестабильной поверхности	🧪 Прототип
🎯 Navigation	Следование за путём с избеганием препятствий	📋 В планах
🧠 RL training	Готовые среды для PPO/SAC	✅ Готово
🦘 Jump & Backflip	Акробатические элементы	✅ Конфиги есть
🦾 Manipulation	Pick & place с манипулятором	⚙️ Частично
```

---

📊 Сенсоры и наблюдения
IMU (гироскоп, акселерометр)

Положения и скорости всех суставов

Контакты стоп с землёй

Команды желаемой скорости

(Опционально) LiDAR, RGBD камера

---

🧠 Обучение с подкреплением
Алгоритмы: PPO, SAC (через RSL-RL)

Многопоточность: до 16384 параллельных сред на одном GPU

Domain randomization: изменение физики, шумы сенсоров

Sim2Real: политики проверены на переносимость (документация)

---

📸 Демо
Здесь будут гифки с ходьбой, кувырком и т.д.
(Вы можете добавить свои после обучения)

---

🗺️ Roadmap
Базовая ходьба и бег

Конфигурация для прыжков

Конфигурация для кувырка

Террейновая рандомизация (пересечённая местность)

Обучение с камерой (vision-based RL)

Sim2Real деплой на реальном Go2

Многоагентное обучение (стайная локомоция)

---

🤝 Как внести вклад
Приветствуются Pull Requests.
Если вы нашли баг или хотите предложить улучшение – создайте Issue.

---

📜 Лицензия
MIT License – свободно для академического и коммерческого использования.

---

⭐ Поддержка
Если вам нравится проект – поставьте звезду на GitHub. Это вдохновляет нас на дальнейшее развитие.

---

👨‍💻 Автор
Grish – AI/ML Engineer

GitHub: @Nersisiian

Специализация: Robotics, Reinforcement Learning, System Design

✨ Сделано с помощью Isaac Lab и ❤️ для сообщества робототехники.

![walking demo](assets/demo_walk.gif)
