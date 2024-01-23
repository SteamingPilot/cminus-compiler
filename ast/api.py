from astnode import *

# **
# * Return a string representation based on the tree grammar
# *
# * @param n an ASTNode
# * @return a char*
def getTreeNodeRep(n):
    print_visitor = PrintVisitor()
    return n.accept(print_visitor)


# **
# * makeProg - Create a $prog node
# *
# * @param vlist a $vlist node
# * @param flist a $flist node
# *
# *              Add vlist if non-NULL
# *              Add flist if non-NULL
# *
# * @return a $prog node
# *
def makeProg(vlist, flist):
    node = ProgNode(vlist, flist)
    return node


# **
# * makeFlist - Create a $flist node
# *
# * @param node  a $flist node
# * @param fdecl a $fdecl node
# *
# *              If node is NULL, create a new $flist node. Otherwise, use node.
# *              Add fdecl if non-NULL
# *
# * @return a $flist node
# *
def makeFlist(node, fdecl):
    if node is None:
        node = FlistNode()
    node.appendChild(fdecl)
    return node

# **
# * makeFdecl - Create a $fdecl node
# *
# * @param node  a $fdecl node
# * @param type  a $type node
# * @param id    a string
# * @param plist a $plist node
# * @param vlist a $vlist node
# * @param stmts a $cmpd node
# *
# *              If node is NULL, create a new $fdecl node. Otherwise, use node.
# *              Add type if non-NULL
# *              Add id if non-NULL
# *              Add plist if non-NULL
# *              Add vlist if non-NULL
# *              Add stmts if non-NULL
# *
# * @return a $fdecl node
# *
def makeFdecl(node, type, id, plist, vlist, stmts):
    if node is None:
        node = FDeclNode()
    node.appendChild(type, id, plist, vlist, stmts)
    return node


# **
# * makePlist - Create a $plist node
# *
# * @param node  a $plist node
# * @param vdecl a $pdecl node
# *
# *              If node is NULL, create a new $plist node. Otherwise, use node.
# *              Add vdecl to node if non-NULL
# *
# * @return a pvlist node
# *
def makePlist(node, pdecl):
    if node is None:
        node = PlistNode()
    node.appendChild(pdecl)
    return node


# **
# * makePdecl - Create a $pdecl node
# *
# * @param type a $type node
# * @param id   a $ident node
# *
# *             Add type to node
# *             Add id to node
# *
# * @return a $vdecl node
# *
def makePdecl(type, id):
    node = PDeclNode(type, id)
    return node


# **
# * makeVlist - Create a $vlist node
# *
# * @param node  a $vlist node
# * @param vdecl a $vdecl node
# *
# *              If node is NULL, create a new $vlist node. Otherwise, use node.
# *              Add id to node if non-NULL
# *
# * @return a $vlist node
# *
def makeVlist(node, vdecl):
    if node is None:
        new_node = VarListNode(vdecl)
        return new_node
    
    node.appendChild(vdecl)
    return node


# **
# * makeVdecl - Create a $vdecl node
# *
# * @param type a $type node
# * @param ids  a $ilist node
# *
# *             Add type to node
# *             Add ids to node
# *
# * @return a $vdecl node
# *
def makeVdecl(type, ids):
    node = VarDecNode(type, ids)
    return node


# **
# * makeIlist - Create a $ilist node
# *
# * @param node a $ilist node
# * @param id   a $ident node
# *
# *             If node is NULL, create a new $ilist node. Otherwise, use node.
# *             Add id to node if non-NULL
# *
# * @return a $ilist node
# *
def makeIlist(node, id):
    if node is None:
        new_node = IlistNode(id)
        return new_node
    
    node.appendChild(id)
    return node


# **
# * makeIdent - Create a $ident node
# *
# * @param id    a string
# * @param dimen a string
# *
# *              Add id
# *              Add dimen if non-NULL
# *
# * @return a $ident node
# *
def makeIdent(id, dimen):
    node = IdentNode(id, dimen)
    return node


# **
# * makeType - make an $type node
# *
# * @param type a string, one of "char", "float", "int", or "void"
# *
# *             Create a new $type node.
# *
# * @return a $type node
# *
def makeType(type):
    node = TypeNode(type)
    return node


# **
# * makeAssign - make an $assign node
# *
# * @param lval a definition
# * @param rval an expression
# *
# *             Create a new $assign node.
# *             Add id to node
# *
# * @return a $assign node
# *
def makeAssign(lval, rval):
    node = AssignNode(lval, rval)
    return node


# **
# * makeVardef - make an $vardef node
# *
# * @param id an identifier
# *
# *           Create a new $vardef node.
# *           Add id to node
# *
# * @return a $vardef node
# *
def makeVardef(id):
    node = VarDefNode(id)
    return node


# **
# * makeArraydef - make an $arraydef node
# *
# * @param id        an identifier
# * @param subscript an expression subscript
# *
# *                  Create a new $arraydef node.
# *                  Add id to node
# *                  Add subscript to node
# *
# * @return a $arraydef node
# *
def makeArraydef(id, subscript):
    node = ArrayDefNode(id, subscript)
    return node


# **
# * makePcall - make an $pcall node
# *
# * @param id   an identifier
# * @param args an $elist node
# *
# *             Create a new $pcall node.
# *             Add id to node
# *             Add args to node
# *
# * @return a $pcall node
# *
def makePcall(id, args):
    node = PCallNode(id, args)
    return node


# **
# * makeIf - Create a $if node
# *
# * @param node a $if node
# * @param test an expression node
# * @param thn  a statement node
# * @param els  a statement node
# *
# *             If node is NULL, create a new $if node. Otherwise, use node.
# *             Add test,thn, and/or els to node if any is non-NULL
# *
# * @return a $if node
# *
def makeIf(node, test, thn, els):
    if node is None:
        node = IfNode()

    node.appendChild(test, thn, els)

    return node


# **
# * makeWhile - make a $while node
# *
# * Create a new $while node.
# *
# * @param expr an expression
# * @param body a statement
# *
# * @return a $while node
# *


def makeWhile(expr, stmt):
    node = WhileNode(expr, stmt)
    return node


# **
# * makeRead - make a $read node
# *
# * Create a new $read node.
# *
# * @param var a variable reference
# *
# * @return a $read node
# *


def makeRead(var):
    node = ReadNode(var)
    return node


# **
# * makeWrite - make a $write node
# *
# * Create a new $write node.
# *
# * @param expr an expression
# *
# * @return a $write node
# *


def makeWrite(expr):
    node = WriteNode(expr)
    return node


# **
# * makeRet - make a $ret node
# *
# * Create a new $ret node.
# *
# * @param expr an expression
# *
# * @return a $ret node
# *


def makeRet(expr):
    node = RetNode(expr)
    return node


# **
# * makeExit - make an $exit node
# *
# * Create a new $exit node.
# *
# * @return a $exit node
# *


def makeExit():
    node = ExitNode()
    return node


# **
# * makeCmpd - Create a $cmpd node
# *
# * @param node a $cmpd node
# * @param stmt a statement node
# *
# *             If node is NULL, create a new $cmpd node. Otherwise, use node.
# *             Add stmt to node
# *
# * @return a $cmpd node
# *
def makeCmpd(node, stmt):
    if node is None:
        node = CmpdNode()

    node.appendChild(stmt)
    return node


# **
# * makeNot - make an $not node
# *
# * @param oper the operand
# *
# *             Create a new $not node.
# *             Add oper to node
# *
# * @return a $not node
# *
def makeNot(oper):
    node = NotNode(oper)
    return node


# **
# * makeOr - make an $or node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $or node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $or node
# *
def makeOr(loper, roper):
    node = OrNode(loper, roper)
    return node


# **
# * makeAnd - make an $and node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $and node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $and node
# *
def makeAnd(loper, roper):
    node = AndNode(loper, roper)
    return node


# **
# * makeEq - make an $eq node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $eq node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $eq node
# *
def makeEq(loper, roper):
    node = EqNode(loper, roper)
    return node


# **
# * makeNe - make an $ne node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $ne node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $ne node
# *
def makeNe(loper, roper):
    node = NeNode(loper, roper)
    return node


# **
# * makeLe - make an $le node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $le node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $le node
# *
def makeLe(loper, roper):
    node = LeNode(loper, roper)
    return node


# **
# * makeLt - make an $lt node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $lt node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $lt node
# *
def makeLt(loper, roper):
    node = LtNode(loper, roper)
    return node


# **
# * makeGe - make an $ge node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $ge node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $ge node
# *
def makeGe(loper, roper):
    node = GeNode(loper, roper)
    return node


# **
# * makeGt - make an $gt node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $gt node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $gt node
# *
def makeGt(loper, roper):
    node = GtNode(loper, roper)
    return node


# **
# * makeAdd - make an $add node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $add node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $add node
# *
def makeAdd(loper, roper):
    node = AddNode(loper, roper)
    return node


# **
# * makeSub - make an $sub node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $sub node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $sub node
# *
def makeSub(loper, roper):
    node = SubNode(loper, roper)
    return node


# **
# * makeMul - make an $mul node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $mul node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $mul node
# *
def makeMul(loper, roper):
    node = MulNode(loper, roper)
    return node


# **
# * makeDiv - make an $div node
# *
# * @param loper the left operand
# * @param roper the right operand
# *
# *              Create a new $div node.
# *              Add loper to node
# *              Add roper to node
# *
# * @return a $div node
# *
def makeDiv(loper, roper):
    node = DivNode(loper, roper)
    return node


# **
# * makeFcall - make an $fcall node
# *
# * @param id   an identifier
# * @param args an $elist node
# *
# *             Create a new $fcall node.
# *             Add id to node
# *             Add args to node
# *
# * @return a $fcall node
# *
def makeFcall(id, args):
    node = FCallNode(id, args)
    return node


# **
# * makeVarref - make an $varref node
# *
# * @param id an identifier
# *
# *           Create a new $varref node.
# *           Add id to node
# *
# * @return a $varref node
# *
def makeVarref(id):
    node = VarRefNode(id)
    return node


# **
# * makeArrayref - make an $arrayref node
# *
# * @param id        an identifier
# * @param subscript an expression subscript
# *
# *                  Create a new $arrayref node.
# *                  Add id to node
# *                  Add subscript to node
# *
# * @return a $arrayref node
# *
def makeArrayref(id, subscript):
    node = ArrayRefNode(id, subscript)
    return node


# **
# * makeStr - make an $str node
# *
# * @param val the string
# *
# *            Create a new $str node.
# *            Add val to node
# *
# * @return a $str node
# *
def makeStr(val):
    node = StrNode(val)
    return node


# **
# * makeCcon - make an $ccon node
# *
# * @param val a string representation of the constant value
# *
# *            Create a new $ccon node.
# *            Add val to node
# *
# * @return an $ccon node
# *
def makeCcon(val):
    node = CConNode(val)
    return node


# **
# * makeFcon - make an $fcon node
# *
# * @param val a string representation of the constant value
# *
# *            Create a new $fcon node.
# *            Add val to node
# *
# * @return an $fcon node
# *
def makeFcon(val):
    node = FConNode(val)
    return node


# **
# * makeIcon - make an $icon node
# *
# * @param val a string representation of the constant value
# *
# *            Create a new $icon node
# *            Add val to node
# *
# * @return an $icon node
# *
def makeIcon(val):
    node = IConNode(val)
    return node


# **
# * makeElist - make an $elist node
# *
# * @param node an $elist node
# * @param expr an expression node
# *
# *             If node is NULL, create a new $elist node. Otherwise, use node.
# *             Add expr to node
# *
# * @return an $elist node
# *
def makeElist(node, expr):
    if node is None:
        node = ElistNode()
    node.appendChild(expr)
    return node