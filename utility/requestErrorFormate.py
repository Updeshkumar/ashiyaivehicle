from config.messages import Messages


def requestErrorMessagesFormate(params):
    
    try:
        for x in params:
            val = params[x]
            return {'error':str(x)+' '+str(val[0])}
    except Exception as e:
        print('................requestErrorMessagesFormate.........',str(e))
        return {'error': 'Invalid Request'}

def arrayErrorMessagesFormate(params):
    
    try:
        for x in params:
            val = params[x]
            return {'error':val[0]}
    except Exception as e:
        print('................requestErrorMessagesFormate.........',str(e))
        return {'error': 'Invalid Request'}

def arrayErrorFormat(errorObj,inputReq):
    for x in errorObj['error']:
        for y in errorObj['error'][x]:
            for i in y:
                y[i] = y[i][0]
            inputReq[x]['error'] = y
    return inputReq
