# .vscode

## Добро пожаловать в мои настройки .vscode

>[!note]
> Возможно, если в документе чего-то не хватает, или я не дописал подробнее, то вы **всегда** можете ознакомиться с настройками.

> [!note]
> ### Главный репозиторий всегда находится в конце этого документа (В каждом документе этой репозитории.)


>[!note]
> ### p.s
> Цвета взял из роблокс студио, почти один в один. 


Сами настройки
```json
{
    "python-envs.defaultEnvManager": "ms-python.python:system",
    "python-envs.pythonProjects": [],
    "editor.tokenColorCustomizations": {
        "functions": "#8fb4ff",
        "strings": "#72e9b6", 
        "numbers": "#FCC419",
        "keywords": "#eb7973",
        "variables": "#64a0de",
        "comments": "#616f81",
        "textMateRules": [
            {
                "scope": "keyword",
                "settings": {
                    "fontStyle": "bold"
                }
            },
            {
                "scope": "variable.other.object",
                "settings": {
                    "foreground": "#7eb4ff"
                }
            }
        ]
    },
    "workbench.colorTheme": "One Dark Pro Darker",
    "workbench.iconTheme": "vscode-icons",
    "editor.fontSize": 20,
    "editor.fontFamily": "Consolas, 'Courier New', monospace",
    "editor.bracketPairColorization.enabled": true,
    "editor.guides.bracketPairs": true,
    "editor.minimap.enabled": true,
    "editor.lineNumbers": "on"
}
```
### 1. `Python` настройки
```json
"python-envs.defaultEnvManager": "ms-python.python:system"
```
**Что делает**: Использует системный `Python` вместо виртуальных окружений.
**Если проще (Чтобы максим понял)**: Берёт `Python` который уже установлен в системе, не заморачивается.
### 2. Список `Python` проектов
```json
"python-envs.pythonProjects": []
```
**Что делает**: Список `Python` проектов (всё)

### 3. Настройки подсветки синтаксиса
```json
"functions": "#8fb4ff"      // Функции - СИНИЙ
"strings": "#72e9b6"        // Строки - ЗЕЛЁНЫЙ  
"numbers": "#FCC419"        // Числа - ЖЁЛТЫЙ
"keywords": "#eb7973"       // Ключевые слова (if, for) - РАСНЫЙ
"variables": "#64a0de"      // Переменные -  ГОЛУБОЙ
"comments": "#616f81"       // Комментарии - СЕРЫЙ
```
TextMate правила (дополнительные)
```json
"keyword": { "fontStyle": "bold" }  // Ключевые слова - ЖИРНЫЕ
"variable.other.object": { "foreground": "#7eb4ff" }  // Объекты - СВЕТЛО-СИНИЙ
```
### 4. Тема и внешний вид (Расширения)
```json
"workbench.colorTheme": "One Dark Pro Darker"
```
**Тема**: [One Dark Pro](https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme)

```json
"workbench.iconTheme": "vscode-icons"
```
**Иконки**: [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)

### 5. Настройки редактора
```json
"editor.fontSize": 20
```
**Размер шрифта**: 20 пикселей
```json
"editor.fontFamily": "Consolas, 'Courier New', monospace"
```
**Шрифт**: *Consolas*

```json
"editor.bracketPairColorization.enabled": true
```
**Цветные скобки**: Чтобы не путать с `()`, `{}` и `[]`

```json
"editor.guides.bracketPairs": true  
```
**Направления для скобок**: Линии показывают какие скобки к каким относится.

```json
"editor.minimap.enabled": true
```
**Миникарта**: Просморт всего файла справа (чтобы искать быстро ошибки)

```json
"editor.lineNumbers": "on"
```
**Номера Строк**: включены

### На этом конец моего документа.


# **[Главный репозиторий](https://github.com/Drugoi-Polz/IservNG)**

>[!warning]
>### ВНИМАНИЕ
> **Главным репозиторием не владею и *никак* не могу редактировать там, что есть.**
