import LoginScreen
import MainScreen
 
LoginScreen.showLoginScreen()

if(LoginScreen.loginCheck):
    MainScreen.connectDb()
    MainScreen.showMainScreen()