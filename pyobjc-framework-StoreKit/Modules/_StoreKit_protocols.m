/*
 * This file is generated by objective.metadata
 *
 * Last update: Mon Mar 18 09:14:47 2013
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1007
    p = PyObjC_IdToPython(@protocol(SKPaymentTransactionObserver));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SKProductsRequestDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SKRequestDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1015 */
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(SKPaymentQueueDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1015 */
}
