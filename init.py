## Sync NukeStudio presets 

execfile('Z:\\pipeline\\nuke\\python\\tom\\T_NukeStudioPresets.py')




#- LAAD PLUGINS & GIZMOS IN------------------------------------------------------------------------------------------------------------------------------------------------------------
path = "Z:/pipeline/nuke_dev/"
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

nuke.pluginAddPath( path + 'icons')
nuke.pluginAddPath( path + 'layouts')
nuke.pluginAddPath( path + 'other')

nuke.pluginAddPath( path + 'gizmos')
nuke.pluginAddPath( path + 'gizmos/wouter')
nuke.pluginAddPath( path + 'gizmos/tom')
nuke.pluginAddPath( path + 'gizmos/roel')
nuke.pluginAddPath( path + 'gizmos/pixelfudger')

nuke.pluginAddPath( path + 'gizmos/nukepedia')
nuke.pluginAddPath( path + 'gizmos/pixomondo')
nuke.pluginAddPath( path + 'gizmos/luma')

nuke.pluginAddPath( path + 'python')
nuke.pluginAddPath( path + 'python/wouter')
nuke.pluginAddPath( path + 'python/')
nuke.pluginAddPath( path + 'python/tom')
nuke.pluginAddPath( path + 'python/nukepedia')


nuke.pluginAddPath( path + 'plugins')
nuke.pluginAddPath( path + 'plugins/3DEqualizer')

nuke.pluginAddPath( path + 'plugins/shotgun')

nuke.pluginAddPath( path + 'plugins/Trapcode')
nuke.pluginAddPath( path + 'TaskPresets')

##execfile("Z:\pipeline\nuke\python\tom\T_NukeStudio_Presetsync.py")