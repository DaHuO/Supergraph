DOWNLOAD_DIR = "/Users/Dom/Downloads/"

def jopen( filename ):
    return open( DOWNLOAD_DIR+filename+".in", "r")

def jout( filename, results, linebreaks=False ):
    f = open(DOWNLOAD_DIR+filename+".out","w")
    for n in range(len(results)):
        f.write( "Case #" + str(n+1) + ": " )
        if isinstance(n, list):
            if linebreaks:
                f.write( "\n" )
            f.write( " ".join(n) )
        else:
            if linebreaks:
                f.write( "\n" )
            f.write( str(results[n]) + "\n" )


