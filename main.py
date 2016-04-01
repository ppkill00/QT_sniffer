## This is for QWidget


from PySide.QtCore import *
from PySide.QtGui import *
import operator

import sys

from Sniffer_UI import *
from Sniffer import *

from scapy.all import *

##self.Sniff_Text_1
##self.Sniff_But_1

class User_MainWidget(QWidget, Ui_Sniffer):
    font = QFont("Courier New" , 8)
    proto_count = {}
    ipsrc_count = {}
    ipdst_count = {}
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        #super(User_MainWidget, self).__init__(parent)
        self.setupUi(self)
        self.Sniff_But_1.clicked.connect(self.handleToggle)
        
        #set font..
        self.Sniff_Text_1.setFont(self.font)
        
        #Worker init 
        self.worker = Worker()
        self.worker.started.connect(self.started)
        self.worker.finished.connect(self.finished)
        self.worker.terminated.connect(self.terminated)
        self.worker.progress.connect(self.updata_main)
        
        '''
        header = ['Src IP','count']
        data = [('192.168.0.1',1),('192.168.10.1',2)]
        table_model = MyTableModel(self,data,header)
        self.TableSrc.setModel(table_model)
        self.TableSrc.setFont(self.font)
        
        header = ['Dst Ip','count']
        data = [('66.66.66.66',12),('0,0,0,0',100)]
        table_model = MyTableModel(self,data,header)
        self.TableDst.setModel(table_model)
        self.TableDst.setFont(self.font)
        '''


    def handleToggle(self):
        if self.worker.isRunning():
            self.worker.continues = False
            self.Sniff_But_1.setEnabled(False)
            while self.worker.isRunning():
                time.sleep(0.01)
                continue
            self.Sniff_But_1.setText("Start")
            self.Sniff_But_1.setEnabled(True)
        else:
            self.worker.continues = True
            self.worker.start()
            self.Sniff_But_1.setEnabled(False)
            while not self.worker.isRunning():
                time.sleep(0.01)
                continue
            self.Sniff_But_1.setText("Stop")
            self.Sniff_But_1.setEnabled(True)

    def updata_main(self,data):
        #print data.split(':')[0]
        #print data.split(':')[1].split('>')[0]
        if len(data) != 0:
            self.update_table()
            self.Sniff_Text_1.appendPlainText(data)
            
            if data.split(':')[0] not in self.proto_count:
                self.proto_count[data.split(':')[0]] = 1
            else:
                self.proto_count[ data.split(':')[0]] += 1

            if data.split(':')[1].split('>')[0] not in self.ipsrc_count:
                self.ipsrc_count[data.split(':')[1].split('>')[0]] = 1
            else:
                self.ipsrc_count[data.split(':')[1].split('>')[0]] += 1

            if data.split(':')[1].split('>')[1] not in self.ipdst_count:
                self.ipdst_count[data.split(':')[1].split('>')[1]] = 1
            else:
                self.ipdst_count[data.split(':')[1].split('>')[1]] += 1
            #print self.ipsrc_count

    def update_table(self):

        header = ['Proto','count']
        proto_table_model = MyTableModel(self,self.proto_count,header)
        self.TableProto.setModel(proto_table_model)
        self.TableProto.setFont(self.font)
        self.TableProto.resizeColumnsToContents()

        header = ['IpSrc','count']
        ipsrc_table_model = MyTableModel(self,self.ipsrc_count,header)
        self.TableSrc.setModel(ipsrc_table_model)
        self.TableSrc.setFont(self.font)
        self.TableSrc.resizeColumnsToContents()
        
        header = ['IpDst','count']
        ipdst_table_model = MyTableModel(self,self.ipdst_count,header)
        self.TableDst.setModel(ipdst_table_model)
        self.TableDst.setFont(self.font)
        self.TableDst.resizeColumnsToContents()
        #Resize Columns and sorting set
        self.TableSrc.setSortingEnabled(True)
        self.TableDst.setSortingEnabled(True)
        self.TableProto.setSortingEnabled(True)

    def started(self):
        print "Worker started " + str(self.worker.currentThreadId())
    def finished(self):
        print "Worker Finished "+ str(self.worker.currentThreadId())
    def terminated(self):
        print "Worker Terminated "+ str(self.worker.currentThreadId())



class MyTableModel(QAbstractTableModel):
    def __init__(self,parent,mydata,header,*args):
        QAbstractTableModel.__init__(self,parent,*args)
        self.mydata = mydata.items()
        self.header = header
        print self.mydata
    def rowCount(self,parent):
        return len(self.mydata)
    def columnCount(self,parent):
        return len(self.header)
        #return len(self.mydata)
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mydata[index.row()][index.column()]
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mydata = sorted(self.mydata,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))


class Worker_Counter(QThread):
    progress = Signal(str)
    def __init__(self,parent = None):
        QThread.__init__(self,parent)
        self.continues = True
        self.counter = U_Counter()
    
    def run(self):
        data = self.counter.start()
        self.progress.emit(data)



class Worker(QThread):
    progress = Signal(str)
    def __init__(self,parent =None):
        #super(updateThread,self).__init__(parent)
        QThread.__init__(self, parent)
        self.continues = True

        self.logic = U_Sniffer()
    def run(self):
        while self.continues:
            #self.msleep(10)
            data = self.logic.start()
            #print data[0].psrc
            #data = str(data).decode('utf-8')
            self.progress.emit(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = User_MainWidget()
    main.show()
    sys.exit(app.exec_())

