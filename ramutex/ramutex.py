
import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('CSEntry'), da.pat.FreePattern('source')])
PatternExpr_1 = da.pat.TuplePattern([da.pat.ConstantPattern('CSReq'), da.pat.FreePattern('source')])
PatternExpr_2 = da.pat.TuplePattern([da.pat.ConstantPattern('Return'), da.pat.FreePattern('test')])
PatternExpr_3 = da.pat.FreePattern('source')
PatternExpr_5 = da.pat.TuplePattern([da.pat.ConstantPattern('Done'), da.pat.BoundPattern('_BoundPattern12_')])
PatternExpr_7 = da.pat.TuplePattern([da.pat.ConstantPattern('Request'), da.pat.FreePattern('timestamp')])
PatternExpr_8 = da.pat.FreePattern('source')
PatternExpr_9 = da.pat.TuplePattern([da.pat.ConstantPattern('Reply'), da.pat.FreePattern('c1'), da.pat.FreePattern('state')])
PatternExpr_10 = da.pat.FreePattern('source')
PatternExpr_11 = da.pat.TuplePattern([da.pat.ConstantPattern('Return'), da.pat.FreePattern('test')])
PatternExpr_12 = da.pat.FreePattern('source')
PatternExpr_6 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Done'), da.pat.BoundPattern('_BoundPattern22_')])])
import sys, os
import time

class X(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_XReceivedEvent_0', PatternExpr_0, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._X_handler_0]), da.pat.EventPattern(da.pat.ReceivedEvent, '_XReceivedEvent_1', PatternExpr_1, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._X_handler_1]), da.pat.EventPattern(da.pat.ReceivedEvent, '_XReceivedEvent_2', PatternExpr_2, sources=[PatternExpr_3], destinations=None, timestamps=None, record_history=None, handlers=[self._X_handler_2])])

    def setup(self, numProcs, test, mainPID):
        self.numProcs = numProcs
        self.mainPID = mainPID
        self.test = test
        self.replies = set()
        self.entryExitTimes = list()
        self.csEntryExitList = list()

    def _da_run_internal(self):
        _st_label_22 = 0
        while (_st_label_22 == 0):
            _st_label_22 += 1
            if (len(self.replies) == self.numProcs):
                _st_label_22 += 1
            else:
                super()._label('_st_label_22', block=True)
                _st_label_22 -= 1
        self.output('Main proc ended number: ', self.entryExitTimes)
        self.output('Checking safety.....')
        self.entryExitTimes = sorted(self.entryExitTimes, key=self.getKey)
        self.output(self.entryExitTimes)
        if self.checkSafety(self.entryExitTimes):
            self.output('Safety check passed')
        else:
            self.output('Safety Failed')
        self.output('In main proc..printing Verifying fairness')
        self.checkFairness(self.csEntryExitList, (2 * self.numProcs))

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

    def checkFairness(self, pids, window):
        windowMap = dict()
        elementToCheck = 0
        for i in range(len(pids)):
            if windowMap.__contains__(pids[i]):
                windowMap[pids[i]] += 1
            else:
                windowMap[pids[i]] = 1
            windowSize = ((i - elementToCheck) + 1)
            if (windowMap[pids[elementToCheck]] <= 1):
                if (windowSize == window):
                    print(((('Failed for ' + str(pids[elementToCheck])) + ' at :') + str(elementToCheck)))
                    return False
            else:
                windowMap[pids[elementToCheck]] -= 1
                elementToCheck += 1
        return True

    def _X_handler_0(self, source):
        self.csEntryExitList.append(source)
    _X_handler_0._labels = None
    _X_handler_0._notlabels = None

    def _X_handler_1(self, source):
        self.csEntryExitList.append(source)
    _X_handler_1._labels = None
    _X_handler_1._notlabels = None

    def _X_handler_2(self, source, test):
        self.replies.add(source)
        self.entryExitTimes.extend(test)
    _X_handler_2._labels = None
    _X_handler_2._notlabels = None

class P(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._PReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_5, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_7, sources=[PatternExpr_8], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_3]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_9, sources=[PatternExpr_10], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_4]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_11, sources=[PatternExpr_12], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_5])])

    def setup(self, ps, nrounds, test, mainPID):
        self.mainPID = mainPID
        self.ps = ps
        self.test = test
        self.nrounds = nrounds
        self.reqc = None
        self.waiting = set()
        self.replied = set()
        self.state = 'Wanted'
        self.startRunningTime = time.time()
        self.test[self.id] = []
        self.csEntryTime = None
        self.csExitTime = None

    def _da_run_internal(self):

        def anounce():
            a = 1
        for i in range(self.nrounds):
            self.cs(anounce)
        self._send(('Done', self.id), self.ps)
        p = None

        def UniversalOpExpr_0():
            nonlocal p
            for p in self.ps:
                if (not PatternExpr_6.match_iter(self._PReceivedEvent_0, _BoundPattern22_=p)):
                    return False
            return True
        _st_label_87 = 0
        while (_st_label_87 == 0):
            _st_label_87 += 1
            if UniversalOpExpr_0():
                _st_label_87 += 1
            else:
                super()._label('_st_label_87', block=True)
                _st_label_87 -= 1
        self._send(('Return', self.test[self.id]), self.mainPID)

    def cs(self, task):
        super()._label('start', block=False)
        self.state = 'Wanted'
        self.reqc = self.logical_clock()
        self._send(('Request', self.reqc), self.ps)
        self._send(('CSReq', self.id), self.mainPID)
        _st_label_69 = 0
        while (_st_label_69 == 0):
            _st_label_69 += 1
            if (len(self.replied) == len(self.ps)):
                _st_label_69 += 1
            else:
                super()._label('_st_label_69', block=True)
                _st_label_69 -= 1
        self.state = 'Held'
        self.csEntryTime = self.logical_clock()
        self._send(('CSEntry', self.id), self.mainPID)
        task()
        super()._label('release', block=False)
        self.state = 'Release'
        self.reqc = None
        self.csExitTime = self.logical_clock()
        self.test[self.id].append((self.csEntryTime, self.csExitTime))
        self._send(('Reply', self.logical_clock(), self.state), self.waiting)
        super()._label('end', block=False)
        self.waiting = set()
        self.replied = set()

    def _P_handler_3(self, timestamp, source):
        if ((self.reqc == None) or ((timestamp, source) < (self.reqc, self.id))):
            self._send(('Reply', self.logical_clock(), self.state), source)
        else:
            self.waiting.add(source)
    _P_handler_3._labels = None
    _P_handler_3._notlabels = None

    def _P_handler_4(self, state, c1, source):
        if ((not (self.reqc is None)) and (c1 > self.reqc)):
            self.replied.add(source)
    _P_handler_4._labels = None
    _P_handler_4._notlabels = None

    def _P_handler_5(self, source, test):
        self.output(('Return from ' + source))
    _P_handler_5._labels = None
    _P_handler_5._notlabels = None

def main():
    nprocs = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
    nrounds = (int(sys.argv[2]) if (len(sys.argv) > 2) else 1)
    da.config(clock='Lamport')
    ps = da.new(P, num=nprocs)
    mainProc = da.new(X, num=1)
    for p in mainProc:
        da.setup({p}, (nprocs, {}, mainProc))
    da.start(mainProc)
    for p in ps:
        da.setup({p}, ((ps - {p}), nrounds, {}, mainProc))
    da.start(ps)
