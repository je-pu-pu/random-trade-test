"""
    「全体がランダムに取引を行うとべき乗分布する」を検証するプログラム
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# fig = plt.figure()
fig, ( a, b ) = plt.subplots( ncols=2, figsize=(16, 9) )

data = [100 for n in range(1000)]

def plot( _ ):
    global data

    for n, _ in enumerate( data ):
        # 全体がランダムにふえる
        # data[ n ] += np.random.randint(1, 10)

        # それぞれの人がランダムな人に size あげる
        size = 1
        # size = 5
        # size = np.random.randint( 0, 10 )
        # size = data[ n ] if data[ n ] < size else size

        if data[ n ] >= size:
            data[ n ] -= size
            data[ np.random.randint( 0, len( data ) ) ] += size
            
        # data[ n ] = np.random.randn()
        # print( data[ n ] )

    data.sort()

    a.cla()
    a.plot( range( 0, len( data ) ), data )

    b.cla()
    b.hist( data, bins=20 )

ani = animation.FuncAnimation( fig, plot, interval=1 )
plt.show()