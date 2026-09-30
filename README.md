# Web UI Test Automation with Playwright

## 📌 Description

Projet d'automatisation de tests UI avec **Playwright et Python**.

L'objectif de ce projet est de mettre en pratique l'automatisation des tests fonctionnels d'une application web, en commençant par la fonctionnalité **Login / Se connecter**.

Le projet est réalisé dans le cadre de mon apprentissage de **Playwright** et s'inscrit dans mon parcours en **QA Automation**.

## 🎯 Application testée

**Practice Test Automation**

Page testée :

https://practicetestautomation.com/practice-test-login/

Fonctionnalité :

**Login / Se connecter**

## 🧪 Périmètre des tests

La première version du projet couvre les scénarios suivants :

* Connexion avec des identifiants valides
* Connexion avec un nom d'utilisateur incorrect
* Connexion avec un mot de passe incorrect

Les cas de test ont été préparés avant l'implémentation de l'automatisation.

## 🛠️ Technologies et outils

* Python
* Playwright
* Chromium
* Firefox
* WebKit
* Git / GitHub

## 📁 Structure du projet

```text
Web UI Test Automation with Playwright/
│
├── .gitignore
├── README.md
├── requirements.txt
├── test_first.py
└── .venv/             
```

## ⚙️ Installation

### 1. Créer l'environnement virtuel

```powershell
python -m venv .venv
```

### 2. Activer l'environnement virtuel

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Installer les dépendances

```powershell
pip install -r requirements.txt
```

### 4. Installer les navigateurs Playwright

```powershell
playwright install
```

## ▶️ Exécution

Les tests seront exécutés depuis l'environnement virtuel :

```powershell
python test_first.py
```

## 📌 Statut du projet

🚧 Projet en cours de développement.

La première étape consiste à mettre en place l'environnement Playwright et à automatiser progressivement les tests de la fonctionnalité Login.
