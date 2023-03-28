def init(t, r):
    """
    function(t, r) {
                t = this.words = t || [],
                this.sigBytes = null != r ? r : 4 * t.length
    }
    """
    ret = {"words": t if t else []}
    if r:
        ret["sigBytes"] = r
    else:
        ret["sigBytes"] = len(ret["words"]) * 4
    return ret
