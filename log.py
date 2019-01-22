from datetime import datetime
import traceback

FILE_LOG = 'log.txt'
class WSLog:

    def logError(self,ex):
        file = open(FILE_LOG, 'a+')
        file.write('\n\n'+'------'+datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\n'+str(ex))
        file.write(traceback.format_exc())

    def log(self,msg):
        file = open(FILE_LOG, 'a+')
        file.write('\n\n'+'------'+datetime.now().strftime('%d/%m/%Y %H:%M:%S')+'\n'+msg)