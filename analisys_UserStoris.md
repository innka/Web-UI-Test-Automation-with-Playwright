# Analyse de la User Story – Se connecter

## Informations générales

**Application:** Practice Test Automation

**Fonctionnalité:** Login

**Rôle utilisateur :** Utilisateur disposant d'un compte

**URL:** `https://practicetestautomation.com/practice-test-login/`

---

# Résumé

En tant qu’utilisateur disposant d’un compte,

Je souhaite me connecter à l’application,

Afin d’accéder à mon espace utilisateur

---

# Description fonctionnelle

L'application met à disposition une page de connexion permettant à un
utilisateur disposant d'un compte de s'authentifier.

La page de connexion contient les éléments suivants :

* Un champ **Username**
* Un champ **Password**
* Un bouton **Submit**

La fonctionnalité de connexion doit permettre de gérer :

* une connexion avec des identifiants valides ;
* une connexion avec un nom d'utilisateur incorrect ;
* une connexion avec un mot de passe incorrect.

Les identifiants fournis pour les tests de la page sont :

* **Username :**`student`
* **Password :**`Password123`

Après une connexion réussie, l'utilisateur est redirigé vers une nouvelle page dont l'URL contient :

`practicetestautomation.com/logged-in-successfully/`

La page de succès doit également contenir un message indiquant que la
connexion a réussi, notamment un texte contenant **« Logged In Successfull»**
et   **« Congratulations student. You successfully logged in »** , ainsi qu'un bouton  **« Log out »** .

En cas d'échec de l'authentification, un message d'erreur correspondant au problème rencontré est affiché.

---

# Critères d'acceptation analysés

## Scénario 1 : Se connecter avec des identifiants valides

### Étant donné

Un utilisateur se trouve sur la page de connexion.

### Quand

L'utilisateur saisit :

* Username : `student`
* Password : `Password123`

et clique sur  **Submit** .

### Alors

* L'utilisateur est redirigé vers une nouvelle page.
* L'URL contient `practicetestautomation.com/logged-in-successfully`.
* Un message confirmant la réussite de la connexion est affiché.
* Le bouton **« Log out »** est visible.

---

## Scénario 2 : Se connecter avec un nom d'utilisateur incorrect

### Étant donné

Un utilisateur se trouve sur la page de connexion.

### Quand

L'utilisateur saisit :

* Username : `incorrectUser`
* Password : `Password123`

et clique sur  **Submit** .

### Alors

* La connexion échoue.
* Un message d'erreur est affiché.
* Le message affiché est : **« Your username is invalid! »**

---

## Scénario 3 : Se connecter avec un mot de passe incorrect

### Étant donné

Un utilisateur se trouve sur la page de connexion.

### Quand

L'utilisateur saisit :

* Username : `student`
* Password : `incorrectPassword`

et clique sur  **Submit** .

### Alors

* La connexion échoue.
* Un message d'erreur est affiché.
* Le message affiché est : **« Your password is invalid! »**

---

# Préconditions identifiées

---

ID                                  Précondition

---

PRE-01                              La page de connexion est accessible.

PRE-02                              Un compte de test valide existe.

PRE-03                              Les identifiants valides du compte de test sont connus.

PRE-04                              Les valeurs invalides nécessaires aux tests négatifs sont disponibles.

PRE-05                              Le champ Username est disponible  sur la page de connexion.

PRE-06                              Le champ Password est disponible sur la page de connexion.

PRE-07 				  Le bouton « Submit » est disponible sur la page de connexion.

---

# Règles métier identifiées

---

ID                                  Règle métier

---

RM-01                               La connexion nécessite un Username et un Password.

RM-02                               Les identifiants `student / Password123` permettent une connexion réussie.

RM-03                               Un nom d'utilisateur incorrect empêche la connexion.

RM-04                               Un mot de passe incorrect empêche la connexion.

RM-05                               Une connexion réussie redirige vers la page de succès.

RM-06                               Après une connexion réussie, l'URL contient `logged-in-successfully/`.

RM-07                               Après une connexion réussie, un message de confirmation est affiché.

RM-08                               Après une connexion réussie, le bouton « Log out » est affiché.

RM-09                               Une erreur de Username affiche le message « Your username is invalid!».

RM-10				 Une erreur de Password affiche le message « Your password is invalid!».

---

# Données d'entrée

Donnée              Valeur                Utilisation

---

Username valide     `student`             Test positif
Password valide     `Password123`         Test positif
Username invalide   `incorrectUser`       Test négatif
Password invalide   `incorrectPassword`   Test négatif

---

# Conditions de test identifiées

Les tests devront couvrir les fonctionnalités suivantes :

* Vérification de l'affichage du champ  **Username** .
* Vérification de l'affichage du champ  **Password** .
* Vérification de l'affichage du bouton  **Submit** .
* Connexion avec des identifiants valides.
* Vérification de la redirection après connexion.
* Vérification de l'URL de la page de succès.
* Vérification du message de confirmation.
* Vérification de la présence du bouton  **« Log out »** .
* Connexion avec un Username incorrect.
* Vérification du message  **« Your username is invalid! »** .
* Connexion avec un Password incorrect.
* Vérification du message  **« Your password is invalid! »** .

---

# Périmètre du premier projet Playwright

Les trois scénarios de connexion fournis par l'application constitueront le **socle fonctionnel principal** :

1. **Positive Login Test**
2. **Negative Username Test**
3. **Negative Password Test**
