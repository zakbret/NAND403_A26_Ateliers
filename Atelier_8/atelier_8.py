import maya.cmds as cmds


def transfert_pivot():
    selection = cmds.ls(selection=True)

    if len(selection) < 2:
        cmds.warning("Sélectionne au moins 2 objets : la source en premier, puis les cibles.")
        return

    source = selection[0]

    pivot_source = cmds.xform(source, query=True, worldSpace=True, rotatePivot=True)

    for objet in selection:
        cmds.xform(objet, worldSpace=True, rotatePivot=pivot_source)
        cmds.xform(objet, worldSpace=True, scalePivot=pivot_source)


transfert_pivot()