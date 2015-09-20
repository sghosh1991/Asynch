
import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('CSEntry'), da.pat.FreePattern('source')])
PatternExpr_1 = da.pat.TuplePattern([da.pat.ConstantPattern('CSReq'), da.pat.FreePattern('source')])
PatternExpr_2 = da.pat.TuplePattern([da.pat.ConstantPattern('Return'), da.pat.FreePattern('test')])
PatternExpr_3 = da.pat.FreePattern('source')
PatternExpr_6 = da.pat.TuplePattern([da.pat.ConstantPattern('ack'), da.pat.FreePattern('c2'), da.pat.BoundPattern('_BoundPattern17_')])
PatternExpr_8 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern('c2'), da.pat.FreePattern('p')])
PatternExpr_9 = da.pat.TuplePattern([da.pat.ConstantPattern('release'), da.pat.FreePattern(None), da.pat.FreePattern('p')])
PatternExpr_12 = da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.BoundPattern('_BoundPattern43_')])
PatternExpr_13 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.BoundPattern('_BoundPattern53_')])])
import sys, time

class X(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_XReceivedEvent_0', PatternExpr_0, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._X_handler_0]), da.pat.EventPattern(da.pat.ReceivedEvent, '_XReceivedEvent_1', PatternExpr_1, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._X_handler_1]), da.pat.EventPattern(da.pat.ReceivedEvent, '_XReceivedEvent_2', PatternExpr_2, sources=[PatternExpr_3], destinations=None, timestamps=None, record_history=None, handlers=[self._X_handler_2])])

    def setup(self, numProcs, test, mainPID, nReq):
        self.mainPID = mainPID
        self.test = test
        self.nReq = nReq
        self.numProcs = numProcs
        self.replies = set()
        self.entryExitTimes = list()
        self.csEntryList = list()
        self.csReqList = list()

    def _da_run_internal(self):
        _st_label_22 = 0
        while (_st_label_22 == 0):
            _st_label_22 += 1
            if (len(self.replies) == self.numProcs):
                _st_label_22 += 1
            else:
                super()._label('_st_label_22', block=True)
                _st_label_22 -= 1
        self.output('Checking safety.....')
        self.entryExitTimes = sorted(self.entryExitTimes, key=self.getKey)
        if self.checkSafety(self.entryExitTimes):
            self.output('Safety check passed')
        else:
            self.output('Safety Failed')
        if self.checkFairness():
            self.output('Fairness passed')
        else:
            self.output('Fairness failed')

    def checkSafety(self, x):
        prev = x[0]
        x = x[1:]
        for interval in x:
            curr = interval
            if (prev[1] >= curr[0]):
                self.output(prev, ':', curr)
                return False
            prev = curr
        return True

    def getKey(self, item):
        return item[0]

    def checkFairness(self):
        start = 0
        end = (start + self.numProcs)
        while (start < len(self.csEntryList)):
            csreq = set()
            csreq.clear()
            for j in range(start, end):
                csreq.add(self.csReqList[j])
            for j in range(start, end):
                if (not (self.csEntryList[j] in csreq)):
                    self.output('Not found', self.csEntryList[j], j, start, end)
                    return False
            start = (start + self.numProcs)
            end = (end + self.numProcs)
        return True

    def _X_handler_0(self, source):
        self.csEntryList.append(source)
    _X_handler_0._labels = None
    _X_handler_0._notlabels = None

    def _X_handler_1(self, source):
        self.csReqList.append(source)
    _X_handler_1._labels = None
    _X_handler_1._notlabels = None

    def _X_handler_2(self, test, source):
        self.replies.add(source)
        self.entryExitTimes.extend(test)
    _X_handler_2._labels = None
    _X_handler_2._notlabels = None

class P(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._PReceivedEvent_0 = []
        self._PReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_6, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_8, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_3]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_9, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_4]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_12, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, s, nrequests, test, mainPID):
        self.mainPID = mainPID
        self.nrequests = nrequests
        self.test = test
        self.s = s
        self.q = set()
        self.startRunningTime = time.time()
        self.test[self.id] = []
        self.csEntryTime = None
        self.csExitTime = None

    def _da_run_internal(self):

        def task():
            a = 1
        for i in range(self.nrequests):
            self.mutex(task)
        self._send(('done', self.id), self.s)
        p = None

        def UniversalOpExpr_3():
            nonlocal p
            for p in self.s:
                if (not PatternExpr_13.match_iter(self._PReceivedEvent_3, _BoundPattern53_=p)):
                    return False
            return True
        _st_label_86 = 0
        while (_st_label_86 == 0):
            _st_label_86 += 1
            if UniversalOpExpr_3():
                _st_label_86 += 1
            else:
                super()._label('_st_label_86', block=True)
                _st_label_86 -= 1
        self._send(('Return', self.test[self.id]), self.mainPID)

    def mutex(self, task):
        super()._label('request', block=False)
        c = self.logical_clock()
        self._send(('request', c, self.id), self.s)
        self._send(('CSReq', self.id), self.mainPID)
        self.q.add(('request', c, self.id))
        p = c2 = None

        def UniversalOpExpr_0():
            nonlocal p, c2
            for (_ConstantPattern10_, c2, p) in self.q:
                if (_ConstantPattern10_ == 'request'):
                    if (not (((c2, p) == (c, self.id)) or ((c, self.id) < (c2, p)))):
                        return False
            return True
        p = c2 = None

        def UniversalOpExpr_1():
            nonlocal p, c2
            for p in self.s:

                def ExistentialOpExpr_2(p):
                    nonlocal c2
                    for (_, _, (_ConstantPattern26_, c2, _BoundPattern28_)) in self._PReceivedEvent_0:
                        if (_ConstantPattern26_ == 'ack'):
                            if (_BoundPattern28_ == p):
                                if (c2 > c):
                                    return True
                    return False
                if (not ExistentialOpExpr_2(p=p)):
                    return False
            return True
        _st_label_65 = 0
        while (_st_label_65 == 0):
            _st_label_65 += 1
            if (UniversalOpExpr_0() and UniversalOpExpr_1()):
                _st_label_65 += 1
            else:
                super()._label('_st_label_65', block=True)
                _st_label_65 -= 1
        self.csEntryTime = self.logical_clock()
        self._send(('CSEntry', self.id), self.mainPID)
        super()._label('critical_section', block=False)
        task()
        super()._label('release', block=False)
        self.csExitTime = self.logical_clock()
        self.test[self.id].append((self.csEntryTime, self.csExitTime))
        self.q.remove(('request', c, self.id))
        self._send(('release', self.logical_clock(), self.id), self.s)

    def _P_handler_3(self, p, c2):
        self.q.add(('request', c2, p))
        self._send(('ack', self.logical_clock(), self.id), p)
    _P_handler_3._labels = None
    _P_handler_3._notlabels = None

    def _P_handler_4(self, p):
        for x in {('request', c, p) for (_ConstantPattern37_, c, _BoundPattern39_) in self.q if (_ConstantPattern37_ == 'request') if (_BoundPattern39_ == p)}:
            self.q.remove(x)
            break
    _P_handler_4._labels = None
    _P_handler_4._notlabels = None

def main():
    nprocs = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
    nrounds = (int(sys.argv[2]) if (len(sys.argv) > 2) else 1)
    da.config(clock='Lamport')
    ps = da.new(P, num=nprocs)
    mainProc = da.new(X, num=1)
    for p in mainProc:
        da.setup({p}, (nprocs, {}, mainProc, nrounds))
    da.start(mainProc)
    for p in ps:
        da.setup({p}, ((ps - {p}), nrounds, {}, mainProc))
    da.start(ps)
