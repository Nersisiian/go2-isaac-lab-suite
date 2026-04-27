# 🤝 Contributing to GO2 Isaac Lab Suite

Спасибо за интерес к проекту! Мы рады любым улучшениям.

## Как помочь

- Сообщить об ошибке – создайте Issue с меткой `bug`.
- Предложить идею – Issue с меткой `enhancement`.
- Исправить код – создайте Pull Request.
- Улучшить документацию – PR с меткой `documentation`.

## Процесс разработки

1. Форкните репозиторий.
2. Создайте ветку: `git checkout -b feature/your-feature-name`
3. Внесите изменения и закоммитьте: `git commit -m "Add: описание"`
4. Запушьте: `git push origin feature/your-feature-name`
5. Откройте Pull Request на GitHub.

## Требования к PR

- Все статус-чеки (build, security) зелёные.
- Код проходит `flake8`.
- Название и описание понятные.

## Локальная проверка

```bash
pip install -r requirements.txt
pip install -e .
flake8 go2_extreme/
Спасибо! 🦾
