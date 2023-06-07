# Abstração 
# Log
# Herança - é um 

class Log:
    def _log(self,msg): #Assinatura do método 
        raise NotImplementedError("Implemente o método log")
    
    def log_error(self,msg):
        return self.log(f'Error: {msg}')

    def log_success(Log):
        def _log(self, msg):
            print(msg)

class LogFileMixin(Log): #Indicar ao desenvolvedor para adicionar funcioanlidades na sua herança múltipla
    #Sendo que essas funcionalidades podem ser provindas de outras classes que são da família do Log    
      
      def _log(self, msg): #Se eu modificar a assinatura desse método 
        #Eu posso quebrar um princípio da programação, denominado de Leskov Substitution Principal
        print(msg)
           
class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)
        print(f'{msg} ({self.__class__.__name__})')



if __name__ == '__main__':
    l = Log()
    l.log('qualquer coisa')







