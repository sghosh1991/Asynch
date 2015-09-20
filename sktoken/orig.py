
import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('exit'), da.pat.FreePattern('source')])
PatternExpr_1 = da.pat.TuplePattern([da.pat.ConstantPattern('entry'), da.pat.FreePattern('source')])
PatternExpr_2 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern('source')])
PatternExpr_4 = da.pat.TuplePattern([da.pat.ConstantPattern('token'), da.pat.FreePattern('Q1'), da.pat.FreePattern('LN1')])
PatternExpr_5 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern('p'), da.pat.FreePattern('n')])
PatternExpr_6 = da.pat.TuplePattern([da.pat.ConstantPattern('token'), da.pat.FreePattern(None), da.pat.FreePattern(None)])
PatternExpr_8 = da.pat.TuplePattern([da.pat.ConstantPattern('token'), da.pat.FreePattern(None), da.pat.FreePattern('LN1')])
PatternExpr_10 = da.pat.TuplePattern([da.pat.ConstantPattern('token'), da.pat.FreePattern(None), da.pat.FreePattern('LN2')])
PatternExpr_13 = da.pat.TuplePattern([da.pat.ConstantPattern('Done')])
PatternExpr_14 = da.pat.BoundPattern('_BoundPattern63_')
PatternExpr_15 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern69_')]), da.pat.TuplePattern([da.pat.ConstantPattern('Done')])])
import sys

class X(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_XReceivedEvent_0', PatternExpr_0, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._X_handler_0]), da.pat.EventPattern(da.pat.ReceivedEvent, '_XReceivedEvent_1', PatternExpr_1, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._X_handler_1]), da.pat.EventPattern(da.pat.ReceivedEvent, '_XReceivedEvent_2', PatternExpr_2, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._X_handler_2])])

    def setup(self, nrounds, nprocs, central):
        self.central = central
        self.nrounds = nrounds
        self.nprocs = nprocs
        self.releases = list()
        self.holds = list()
        self.requests = list()

    def _da_run_internal(self):
        self.output('Inside Main', self.nprocs, self.nrounds)
        _st_label_38 = 0
        while (_st_label_38 == 0):
            _st_label_38 += 1
            if (len(self.releases) == (self.nprocs * self.nrounds)):
                _st_label_38 += 1
            else:
                super()._label('_st_label_38', block=True)
                _st_label_38 -= 1
        self.output('Calling check')
        if self.checkSafety():
            self.output('SAFETY CHECK PASSED')
        else:
            self.output('SAFETY CHECK FAILED')
        if self.checkFairness():
            self.output('Fairness CHECK PASSED')
        else:
            self.output('Fairness CHECK FAILED')
        self.output('Main ended')

    def checkFairness(self):
        self.output('CHECKING', len(self.requests), len(self.holds))
        j = 0
        if (not (self.requests[0] == self.holds[j])):
            while (not (self.holds[j] == self.requests[0])):
                j = (j + 1)
        i = 0
        while (i < len(self.requests)):
            if ((i < (len(self.requests) - 1)) and (self.requests[i] == self.requests[(i + 1)])):
                i = (i + 1)
                continue
            self.output('checking', self.requests[i], self.holds[j])
            if (not (self.requests[i] == self.holds[j])):
                return False
            while ((j < len(self.holds)) and (self.holds[j] == self.requests[i])):
                j = (j + 1)
            i = (i + 1)
        return True

    def checkSafety(self):
        if (not (len(self.releases) == len(self.holds))):
            return False
        i = 0
        for process in self.releases:
            self.output('checking', process)
            if (not (process == self.holds[i])):
                return False
            i = (i + 1)
        return True

    def _X_handler_0(self, source):
        self.releases.append(source)
    _X_handler_0._labels = None
    _X_handler_0._notlabels = None

    def _X_handler_1(self, source):
        self.holds.append(source)
        self.output('Added entry', source)
    _X_handler_1._labels = None
    _X_handler_1._notlabels = None

    def _X_handler_2(self, source):
        self.requests.append(source)
        self.output('Added request', source)
    _X_handler_2._labels = None
    _X_handler_2._notlabels = None

class P(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._PSentEvent_2 = []
        self._PReceivedEvent_3 = []
        self._PSentEvent_4 = []
        self._PReceivedEvent_5 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_4, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_3]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_5, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_4]), da.pat.EventPattern(da.pat.SentEvent, '_PSentEvent_2', PatternExpr_6, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_8, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_PSentEvent_4', PatternExpr_10, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_5', PatternExpr_13, sources=[PatternExpr_14], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, ps, orig_token, nrounds, central):
        self.central = central
        self.ps = ps
        self.orig_token = orig_token
        self.nrounds = nrounds
        self.RN = dict(((p, 0) for p in self.ps))
        self.Q = []
        self.LN = dict(((p, 0) for p in self.ps))

    def _da_run_internal(self):

        def anounce():
            self.output('In cs!')
        if self.haveToken():
            self._send(('request', self.id), self.central)
            self.output("I'm lucky!")
        for i in range(self.nrounds):
            self.cs(anounce)
        self._send(('Done',), self.ps)
        p = None

        def UniversalOpExpr_3():
            nonlocal p
            for p in self.ps:
                if (not PatternExpr_15.match_iter(self._PReceivedEvent_5, _BoundPattern69_=p)):
                    return False
            return True
        _st_label_92 = 0
        while (_st_label_92 == 0):
            _st_label_92 += 1
            if UniversalOpExpr_3():
                _st_label_92 += 1
            else:
                super()._label('_st_label_92', block=True)
                _st_label_92 -= 1
        self.output('Done!')

    def cs(self, task):
        super()._label('request', block=False)
        if (not self.haveToken()):
            self.RN[self.id] += 1
            self._send(('request', self.id, self.RN[self.id]), self.ps)
            self._send(('request', self.id), self.central)
            _st_label_65 = 0
            while (_st_label_65 == 0):
                _st_label_65 += 1
                if self.haveToken():
                    _st_label_65 += 1
                else:
                    super()._label('_st_label_65', block=True)
                    _st_label_65 -= 1
        self._send(('entry', self.id), self.central)
        task()
        self._send(('exit', self.id), self.central)
        self.LN[self.id] = self.RN[self.id]
        self.Q.extend([p for p in self.ps if (not (p in self.Q)) if (self.RN[p] == (self.LN[p] + 1))])
        if (len(self.Q) > 0):
            p = self.Q.pop()
            self._send(('token', self.Q, self.LN), p)

    def haveToken(self):

        def ExistentialOpExpr_0():
            for (_, _, (_ConstantPattern29_, _, _)) in self._PSentEvent_2:
                if (_ConstantPattern29_ == 'token'):
                    if True:
                        return True
            return False
        LN1 = LN2 = None

        def ExistentialOpExpr_1():
            nonlocal LN1, LN2
            for (_, _, (_ConstantPattern43_, _, LN1)) in self._PReceivedEvent_3:
                if (_ConstantPattern43_ == 'token'):

                    def ExistentialOpExpr_2(LN1):
                        nonlocal LN2
                        for (_, _, (_ConstantPattern57_, _, LN2)) in self._PSentEvent_4:
                            if (_ConstantPattern57_ == 'token'):
                                if (LN2[self.id] > LN1[self.id]):
                                    return True
                        return False
                    if (not ExistentialOpExpr_2(LN1=LN1)):
                        return True
            return False
        return ((self.orig_token and (not ExistentialOpExpr_0())) or ExistentialOpExpr_1())

    def _P_handler_3(self, LN1, Q1):
        self.Q = Q1
        self.LN = LN1
    _P_handler_3._labels = None
    _P_handler_3._notlabels = None

    def _P_handler_4(self, n, p):
        self.RN[p] = max((self.RN[p], n))
        if (self.haveToken() and (self.RN[p] == (self.LN[p] + 1))):
            self._send(('token', self.Q, self.LN), p)
    _P_handler_4._labels = None
    _P_handler_4._notlabels = None

def main():
    nprocs = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
    nrounds = (int(sys.argv[2]) if (len(sys.argv) > 2) else 1)
    central = da.new(X, num=1)
    for p in central:
        da.setup({p}, (nrounds, nprocs, central))
    da.start(central)
    ps = da.new(P, num=nprocs)
    lucky = ps.pop()
    da.setup(ps, ((ps | {lucky}), False, nrounds, central))
    da.setup({lucky}, ((ps | {lucky}), True, nrounds, central))
    da.start((ps | {lucky}))
