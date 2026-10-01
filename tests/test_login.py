# test_login.py

# test pour vérifier l'affichage des champs du formulaire de login
def test_01_username_field_is_visible(login_page):
    login_page.verify_username_visible()

# Cas de test - LOGIN-02 - Vérifier l'affichage du champ Password
def test_02_password_field_is_visible(login_page):
    login_page.verify_password_visible()

# Cas de test - LOGIN-03 - Vérifier l'affichage du bouton Submit
def test_03_submit_button_is_visible(login_page):
    login_page.verify_submit_button_visible()

# Cas de test - LOGIN-04 - Se connecter avec des identifiants valides
def test_04_se_connecter_avec_identifiants_valides(login_page):
    valid_login = login_page.login("student", "Password123")
    valid_login.verify_page_url()
    #assert login_page.page.url == "https://practicetestautomation.com/logged-in-successfully/"

#Cas de test - LOGIN-05 - Vérifier le message « Logged In Successfully »
def test_05_message_logged_in_successfully(login_page):
    valid_login = login_page.login("student", "Password123")
    valid_login.verify_login_success_visible()

#Cas de test - LOGIN-06 - Vérifier le message de félicitations après connexion
def test_06_message_felicitations_connexion(login_page):
    valid_login = login_page.login("student", "Password123")
    valid_login.verify_success_text_visible()

#Cas de test - LOGIN-07 - Vérifier l'affichage du bouton Log out
def test_07_bouton_log_out_visible(login_page):
    valid_login = login_page.login("student", "Password123")
    valid_login.verify_logout_button_visible()

#Cas de test - LOGIN-08 - Se connecter avec un nom d'utilisateur incorrect
def test_08_se_connecter_avec_nom_utilisateur_incorrect(login_page):
    # Implémenter le test pour vérifier le comportement en cas de nom d'utilisateur incorrect
    invalid_login = login_page.login("wronguser", "Password123") 
    # Vérifier que le message d'erreur approprié est affiché "Your username is invalid!"
    invalid_login.error_message_incorrect_username()

#Cas de test - LOGIN-09 - Se connecter avec un mot de passe incorrect
def test_09_se_connecter_avec_mot_de_passe_incorrect(login_page):
    # Implémenter le test pour vérifier le comportement en cas de mot de passe incorrect
    invalid_password = login_page.login("student", "WrongPassword") 
    # Vérifier que le message d'erreur approprié est affiché "Your password is invalid!"
    invalid_password.error_message_incorrect_password()

#Cas de test - LOGIN-10 - Vérifier l'échec de connexion avec un Username incorrect (reste sur la page de connexion)
def test_10_echec_connexion_username_incorrect(login_page):
    invalid_login = login_page.login("", "Password123") 
    # Vérifier que l'URL reste sur la page de connexion
    assert invalid_login.page.url == "https://practicetestautomation.com/practice-test-login/"

#Cas de test - LOGIN-11 - Vérifier l'échec de connexion avec un Password incorrect (reste sur la page de connexion)
def test_11_echec_connexion_password_incorrect(login_page):
    invalid_password = login_page.login("student", "") 
    # Vérifier que l'URL reste sur la page de connexion
    assert invalid_password.page.url == "https://practicetestautomation.com/practice-test-login/"

