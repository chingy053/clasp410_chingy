#!/usr/bin/env python3

'''
A module for burning forests .
'''
#---------------------------------------------------------------
import os
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation, PillowWriter
import inspect
#---------------------------------------------------------------

def forest_fire(isize=3, jsize=3, nstep=4, case='fire',pspread=1.0, pignite=0.0, pbare=0, pfetal=0):
    '''
    Create a forest fire.

    Parameters
    ------------
    isize, jsize : int, defaults to 3
        Set size of forest in x and y direction, respectively.
    nstep : int, defaults to 4
        Set number of steps to advance solution.
    case : string
        Set the case of pseudo-stochastic processes. Set to "fire" for wildfire or set to "disease" for spread of infection diseases.
    pspread : float, defaults to 1.0
        Set chance that fire can spread in any direction, from 0 to 1
        (i.e., 0% to 100% chance of spread.)
    pignite : float, defaults to 0.0
        Set the chance that a point starts the simulation on fire (or infected)
        from 0 to 1 (0% to 100%).
    pbare : float, defaults to 0.0
        Set the chance that a point starts the simulation on bare (or
        immune) from 0 to 1 (0% to 100%).
    pfetal : float, defaults to 0.0
        Set the chance that a person did not survive the disease spread from 0 to 1 (0% to 100%). Only used in the disease case.

    Returns
    ------------
    forest : Numpy array
        Solution of forest fire with size of [time x y-dimension x x-dimension], where 1 indicates bare land (after burning), 2 indicates forest, and 3 indicates fire.
    '''

    # Creating a forest and making all spots have trees.
    forest = np.zeros((nstep, isize, jsize)) + 2

    # Set initial conditions for BURNING/INFECTED and BARE/IMMUNE
    # Start with BURNING/INFECTED:
    if pignite > 0:  # Scatter fire randomly:
        loc_ignite = np.zeros((isize, jsize), dtype=bool)
        while loc_ignite.sum() == 0:
            loc_ignite = rand(isize, jsize) <= pignite
        print(f"Starting with {loc_ignite.sum()} points on fire or infected.")
        forest[0, loc_ignite] = 3
    else:
        # Set initial fire to center:
        forest[0, isize//2, jsize//2] = 3

    # Set bare land/immune people:
    loc_bare = rand(isize, jsize) <= pbare
    forest[0, loc_bare] = 1

    # Initialize variable before the loop
    full_burn_time = None

    # Loop through time to advance our fire.
    for k in range(nstep-1):
        # Assume the next time step is the same as the current:
        forest[k+1, :, :] = forest[k, :, :]
        # Search every spot that is on fire and spread fire as needed.
        for i in range(isize):
            for j in range(jsize):

                # Are we on fire?
                if forest[k, i, j] != 3:
                    continue
                # Ah! it burns. Spread fire in each direction.
                # Need to flip axis in plot if use pcolor
                # Spread "up" (i to i-1)
                if (pspread > rand()) and (i > 0) and (forest[k, i-1, j] == 2):
                    forest[k+1, i-1, j] = 3
                # Spread "Down"
                if (pspread > rand()) and (i < isize-1) and (forest[k, i+1, j] == 2):
                    forest[k+1, i+1, j] = 3
                # Spread "East"
                if (pspread > rand()) and (j < jsize-1) and (forest[k, i, j+1] == 2):
                    forest[k+1, i, j+1] = 3
                # Spread "West"
                if (pspread > rand()) and (j > 0) and (forest[k, i, j-1] == 2):
                    forest[k+1, i, j-1] = 3

                if case == 'fire':
                    # Change buring to burnt:
                    forest[k+1, i, j] = 1
                elif case == 'disease':
                    if np.random.rand() <= pfetal:
                        # Change from sick to dead:
                        forest[k+1, i, j] = 0
                    else:
                        # Survive the disease:
                        forest[k+1, i, j] = 1

        # Save the time where fire is out
        if not np.any(forest[k, :, :] == 3) and full_burn_time is None:
            full_burn_time = k
    # if full_burn_time is not None:
    #     print(f"The fire extinguished at timestep {full_burn_time + 1}.")
    # else:
    #     print("The fire never extinguished within the simulation time.")

    return forest, full_burn_time

def plot_progression(forest, fig=None, ax=None, save_dir=None, save_name=None):
    '''
    Calculate the time dynamics of a forest fire and plot them.
    y-axis = Fraction of area where the condition is either burnt/immuned, forest/healthy, burning/infected.
    x-axis = Time

    Parameters
    ----------
    forest : np.ndarray
        3D array (time, y, x) representing simulation states.
    fig : matplotlib.figure.Figure, optional
        Existing figure to draw on. If None, a new figure is created.
    ax : matplotlib.axes.Axes, optional
        Axis object to draw on. If None, a new axis is created.
    
    '''
    ksize, isize, jsize = forest.shape
    npoints = isize * jsize
    time = np.arange(ksize)

    # Calculate percentages for each category
    perc_burnt = 100 * np.sum(forest == 1, axis=(1, 2)) / npoints
    perc_forest = 100 * np.sum(forest == 2, axis=(1, 2)) / npoints
    perc_burning = 100 * np.sum(forest == 3, axis=(1, 2)) / npoints

    # Create fig/ax if not provided
    if fig is None or ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))

    # Plot progression
    ax.plot(time, perc_burnt, label="Burnt", color="brown", linewidth=2)
    ax.plot(time, perc_forest, label="Forest", color="green", linewidth=2)
    ax.plot(time, perc_burning, label="Burning", color="red", linewidth=2)
    
    ax.set_xlabel("Time (steps)")
    ax.set_ylabel("Percentage of Total Area")
    ax.set_title("Progression of Forest Fire / Disease Spread")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)
    
    plt.tight_layout()

    return fig, ax

def plot_forest2d(isize=3, jsize=3, nstep=4, 
                  case='fire', 
                  pspread=1.0, pignite=0.0, pbare=0.0, pfetal=0.0,
                  fig=None,
                  ax=None,
                  txt_label = False,
                  save_dir=None, save_name=None,
                  **kwargs):
    '''
    This function plots each frame of the forest or disease spread simulation in PNG and saves the PNG in the current directory. The plotting automatically stops at the frame where the entire forest is burnt or the disease has completely spread.

    Parameters
    ------------
    isize, jsize : int, defaults to 3
        Set size of forest in x and y direction, respectively.
    nstep : int, defaults to 4
        Set number of steps to advance solution.
    case : string
        Set the case of pseudo-stochastic processes. Set to "fire" for wildfire or set to "disease" for spread of infection diseases.
    fig : matplotlib.figure.Figure, optional
        Existing figure to plot on. If None, a new figure is created.
    ax : matplotlib.axes.Axes, optional
        Existing axes to plot on. If None, new axes are created.
    txt_label : bool, default True
        Whether to display text labels for each cell (e.g., "Bare", "Forest", "Fire").
    save_dir : str, optional
        Folder path to save the figure. If None, figure is not saved.
    save_name : str, optional
        Custom filename for the figure (without extension).
    **kwargs : dict, optional
        Additional keyword arguments passed to the plotting function.    
        
    Returns
    ------------
    fig, ax : Matplotlib figure & axes objects,
        The figure and axes of the plot.

    '''
    if case == 'fire':
        forest_cmap = ListedColormap(['tan', 'darkgreen', 'crimson'])
        names = {1: "Bare", 2: "Forest", 3: "Fire"}
        forest,_ = forest_fire(isize=isize, jsize=jsize, nstep=nstep,**kwargs)
        set_vmin = 1
        set_vmax = 3
    elif case == 'disease':
        forest_cmap = ListedColormap(['gray', 'deepskyblue', 'orange', 'red'])
        names = {0: "Deceased", 1: "Immuned", 2: "Healthy", 3: "Sick"}
        forest,_ = forest_fire(isize=isize, jsize=jsize, nstep=nstep,case='disease',**kwargs)
        set_vmin = 0
        set_vmax = 3

    for k in range(nstep):
        # Create fig and ax
        created_ax = False
        if ax is None or fig is None:
            fig, ax = plt.subplots(figsize=(10, 8))
            created_ax = True

        # Plot
        im = ax.pcolor(forest[k], cmap=forest_cmap, vmin=set_vmin, vmax=set_vmax)
        ax.set_title(f"Timestep = {k}\n \
                     p_spread = {pspread}, p_bare = {pbare}, p_ignite = {pignite}",
                    fontsize=14, loc='center')

        # Label each cell
        if txt_label == True:
            for i in range(isize):
                for j in range(jsize):
                    ax.text(j + 0.5, i + 0.5, names[int(forest[k, i, j])],
                            ha="center", va="center", fontsize=12, color="black")

        # Add colorbar if newly created fig
        if created_ax:
            cbar = fig.colorbar(im, ax=ax, ticks=np.arange(set_vmin, set_vmax+1), orientation="horizontal", pad=0.1)
            cbar.ax.set_xticklabels([names[t] for t in np.arange(set_vmin, set_vmax + 1)])
            cbar.ax.tick_params(axis='x', which='both', bottom=False, top=False)
        ax.set_xlabel("Eastward (km) $\\longrightarrow$")
        ax.set_ylabel("NOrthward (km) $\\longrightarrow$")
        ax.invert_yaxis()
        fig.tight_layout()

        # Save frame
        if save_dir is not None and save_name is not None:
            # Create directory if it doesn't exist
            os.makedirs(save_dir, exist_ok=True)
            save_path = os.path.join(save_dir, f"{save_name}_{k}.png")
            fig.savefig(save_path)

        # Close only if this function created the fig
        if created_ax:
            plt.close(fig)
            ax.clear()
        else:
            ax.clear()  # if using external subplot, clear for next timestep

        # Check if there is any 3
        if not np.any(forest[k, :, :] == 3):
            print(f"Plotting stopped: Fire/disease has stopped spreading at time = {k+1}")
            break
    return fig, ax

def plot_forest2d_animation(isize=3, jsize=3, nstep=4, 
                  case='fire', 
                  fig=None,
                  ax=None,
                  txt_label = False,
                  fps=4, interval_ms=250,
                  save_dir=None, save_name=None,
                  **kwargs):
    '''
    This function plots each frame of the forest or disease spread simulation, combines them into a GIF, and saves the GIF in the current directory.

    Parameters
    ------------
    isize, jsize : int, defaults to 3
        Set size of forest in x and y direction, respectively.
    nstep : int, defaults to 4
        Set number of steps to advance solution.
    case : string
        Set the case of pseudo-stochastic processes. Set to "fire" for wildfire or set to "disease" for spread of infection diseases.
    fig : matplotlib.figure.Figure, optional
        Existing figure to plot on. If None, a new figure is created.
    ax : matplotlib.axes.Axes, optional
        Existing axes to plot on. If None, new axes are created.
    txt_label : bool, default True
        Whether to display text labels for each cell (e.g., "Bare", "Forest", "Fire").
    fps : int, default 4
        Frames per second when saving the GIF.
    interval_ms : int, default 250
        Delay between frames in milliseconds.
    save_dir : str, optional
        Folder path to save the figure. If None, figure is not saved.
    save_name : str, optional
        Custom filename for the figure (without extension).
    **kwargs : dict, optional
        Additional keyword arguments passed to the plotting function.    
        
    Returns
    ------------
    fig, ax : Matplotlib figure & axes objects,
        The figure and axes of the plot.
    ani : gif animation 
        A gif plot of fire/disease spreading through the space over time.
    '''

    # Set a case
    if case == 'fire':
        forest_cmap = ListedColormap(['tan', 'darkgreen', 'crimson'])
        names = {1: "Bare", 2: "Forest", 3: "Fire"}
        forest,_ = forest_fire(isize=isize, jsize=jsize, nstep=nstep,**kwargs)
        set_vmin = 1
        set_vmax = 3
    elif case == 'disease':
        forest_cmap = ListedColormap(['gray', 'deepskyblue', 'orange', 'red'])
        names = {0: "Deceased", 1: "Immuned", 2: "Healthy", 3: "Sick"}
        forest,_ = forest_fire(isize=isize, jsize=jsize, nstep=nstep,case='disease',**kwargs)
        set_vmin = 0
        set_vmax = 3

    # Create figure and set of axes:
    if ax is None:
        fig, ax = plt.subplots(1,1, figsize = (10,8))
        
    # Create a figure at t = 0
    im = ax.pcolor(forest[0, :, :], cmap=forest_cmap, vmin=set_vmin, vmax=set_vmax)
    ttl = ax.set_title("Timestep = 0")
    
    texts = []
    if txt_label == True:
        for i in range(isize):
            row = []
            for j in range(jsize):
                t = ax.text(j + 0.5, i + 0.5, names[int(forest[0, i, j])],
                            ha="center", va="center", fontsize=12, color="black")
                row.append(t)
            texts.append(row)

    # Create Colorbar
    cbar = fig.colorbar(im, ax=ax, ticks=np.arange(set_vmin, set_vmax + 1), orientation="horizontal", pad=0.10)
    cbar.ax.set_xticklabels([names[k] for k in np.arange(set_vmin, set_vmax + 1)])
    cbar.ax.tick_params(axis='x', which='both', bottom=False, top=False)
    
    # Update the frame with rest of the t
    def update(frame):
        im.set_array(forest[frame, :, :].ravel())
        ttl.set_text(f"Timestep = {frame}")

        if txt_label == True:
            F = forest[frame, :, :]
            for i in range(isize):
                for j in range(jsize):
                    texts[i][j].set_text(names[int(F[i, j])])

        # Check if all elements are 1
        if not np.any(forest[frame, :, :] == 3):
            try:
                ani.event_source.stop()
                print(f"Plotting stopped: all spaces are burning/infected at time = {frame}")
            except:
                pass  # Ignore the error
        
        if txt_label == True:
            return (im, ttl, *[t for row in texts for t in row])
        else:
            return (im, ttl)

    ani = FuncAnimation(fig, update, frames=nstep, interval=interval_ms, blit=False)
    ax.set_xlabel("Eastward (km) $\\longrightarrow$")
    ax.set_ylabel("NOrthward (km) $\\longrightarrow$")
    ax.invert_yaxis()

    fig.tight_layout()
    plt.rcParams.update({'font.size': 16})
    plt.show()


    # Save frame
    if save_dir is not None and save_name is not None:
        # Create directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, f"{save_name}.gif")
        ani.save(save_path, writer=PillowWriter(fps=fps))

    return fig, ax, ani

#============Q1
# forest_fire(nstep=7)
# plot_forest2d(nstep=7)
# plot_forest2d_animation(nstep=7)

# plot_forest2d(isize=10,jsize=15,nstep=20)
# plot_forest2d_animation(isize=10,jsize=15,nstep=20,txt_label = False)
# plot_forest2d_animation(isize=100, jsize=100, nstep=20, pspread=0.6, pignite=0.05, pbare=0)

#============Q3
# forest_fire(nstep=7,case='disease')
# plot_forest2d_animation(isize=100, jsize=100, nstep=20,case='disease', pspread=0.6, pignite=0.05, pbare=0,pfetal=0.05)


# plot_forest2d_animation(isize=100, jsize=100, nstep=20, pspread=0.65, pignite=0.05, pbare=0.05)
# plot_forest2d_animation(isize=100, jsize=100, nstep=40, case='disease' ,pspread=0.65, pignite=0.05, pbare=0.05, pfetal=0.85)



