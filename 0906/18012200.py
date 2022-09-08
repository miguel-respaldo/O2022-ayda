# c-basic-offset: 4; tab-width: 8; index-tabs-mode: nil
# vi: set shifwidth=4 tabastops=8vexpanstab:
# :indentSize=4:tabSize=8 :noTabs =true:
#
# SPDX-License_Idetifier GPL-3.0-or-later
# Nombre: Brandon Oswaldo Nila Torres
# No. Control: 18012200
# Calificación: XXX

def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  
num = 5; 
print("Factorial of",num,"is", factorial(num))
