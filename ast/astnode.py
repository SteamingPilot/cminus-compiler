# GLOBAL VARIABLE FOR CONSTANT
## DATA TYPES
DT_VOID = 0
DT_INT = 1
DT_FLOAT = 2
DT_CHAR = 3
DT_NONE = 4
DT_ARRAY_INT = 5
DT_ARRAY_FLOAT = 6
DT_ARRAY_CHAR = 7
DT_STR = 8


## ERROR TYPES (Error codes start from 400)
ERROR_ARITH = 400
ERROR_UND = 401
ERROR_BOOL = 402
ERROR_CMP = 403
ERROR_DMUL = 404
ERROR_UNR = 405
ERROR_NRT = 406
ERROR_PRM = 407
ERROR_BND = 408
ERROR_SUB = 409
ERROR_DIM = 410
ERROR_RTT = 411
ERROR_VRT = 412
ERROR_FNP = 413
ERROR_NFN = 414
ERROR_PRF = 415
ERROR_NPR = 416

# Data Type for Function
# For each function we will add a new data type for that function.
# They will be all integer starting from 1000.
DT_FUNCTION_COUNTER = 1000

# Index Uses

# Coersion table indices
# Arithmatic
INDEX_COERSION_ADD = 0
INDEX_COERSION_SUB = 0
INDEX_COERSION_MUL = 0
INDEX_COERSION_DIV = 0
# AND, OR Operation
INDEX_COERSION_AND = 1
INDEX_COERSION_OR = 1
# Relational Operations
INDEX_COERSION_RELATIONAL = 2
INDEX_COERSION_LT = 2
INDEX_COERSION_LTE = 2
INDEX_COERSION_GT = 2
INDEX_COERSION_GTE = 2
INDEX_COERSION_EQ = 2
INDEX_COERSION_NEQ = 2

# Stack Frame
INDEX_STACK_FUNCTIONS = 0
INDEX_STACK_GLOBALS = 1

INDEX_STACK_FUNCTIONS_RETURN = 0
INDEX_STACK_FUNCTIONS_DTYPE = 1
INDEX_STACK_FUNCTIONS_HAS_RETURNED = 2

INDEX_ST_FR_VDECL_TYPE = 0
INDEX_ST_FR_VDECL_POINTER = 1
INDEX_ST_FR_VDECL_IS_REFERENCED = 2

# Index for Dimension Array in ident Node
INDEX_DIM_ARA_IDENT_TYPE = 0
INDEX_DIM_ARA_IDENT_BOUND = 1


# Other Indices

# Indices of the list that is insterted in the plist argument type when the data type is an array. 
INDEX_PLIST_ARA_PR_DT = 0
INDEX_PLIST_ARA_IND_DT = 1
INDEX_PLIST_ARA_IND_BND = 2


IDX_FNODE_PROP_TYPE = "type" 
IDX_FNODE_PROP_ID = "id"
IDX_FNODE_PROP_PLIST = "plist"
IDX_FNODE_PROP_VLIST = "vlist"
IDX_FNODE_PROP_STMTS = "stmts"


# This will be used to check whether someone returned an error or not
ERRORS = {
    ERROR_UND: True,
    ERROR_ARITH: True,
    ERROR_BOOL: True,
    ERROR_CMP: True,
    ERROR_DMUL: True,
    ERROR_UNR: True,
    ERROR_NRT: True,
    ERROR_PRM: True,
    ERROR_RTT: True,
    ERROR_VRT: True,
    ERROR_BND: True,
    ERROR_SUB: True,
    ERROR_DIM: True,
    ERROR_FNP: True,
    ERROR_NFN: True,
    ERROR_PRF: True,
    ERROR_NPR: True
}


# This is used by our PrintVisitor
map_dtToPrint = {
    DT_INT: "int",
    DT_FLOAT: "float",
    DT_CHAR: "char",
    DT_STR: "str",
    DT_VOID: "void",
    DT_NONE: "none",
    DT_ARRAY_INT: "int",
    DT_ARRAY_CHAR: "char",
    DT_ARRAY_FLOAT: "float",
    ERROR_ARITH: "error_arith",
    ERROR_UND: "error_und",
    ERROR_BOOL: "error_bool",
    ERROR_CMP: "error_cmp",
    ERROR_DMUL: "error_dmul",
    ERROR_UNR: "error_unr",
    ERROR_NRT: "error_nrt",
    ERROR_PRM: "error_prm",
    ERROR_BND: "error_bnd",
    ERROR_SUB: "error_sub",
    ERROR_DIM: "error_dim",
    ERROR_RTT: "error_rtt",
    ERROR_VRT: "error_vrt",
    ERROR_FNP: "error_fnp",
    ERROR_NFN: "error_nfn",
    ERROR_PRF: "error_prf",
    ERROR_NPR: "error_npr"
}

# Dynamic Funtion DataType Mapper
function_dt_mapper = dict()



# Constants for the CompileVisitor

# Others
# Data Type Sizes
DT_SIZE_INT = 8
DT_SIZE_FLOAT = 8
DT_SIZE_CHAR = 8
DT_DBL_PR_FLOAT_DIFF = 4


STACK_ALIGNMENT = 16

REG_INT = 0
REG_FLOAT = 1

REG_SET_ALL = 0
REG_SET_CALLEE_SAVED = 1

FUNC_ARG_CVT_DT_I_TO_F = 0
FUNC_ARG_CVT_DT_F_TO_I = 1

FUNC_ARG_CND_CD_GEN_SELF = 0
FUNC_ARG_CND_CD_GEN_OTHER = 1

GLOBAL_DATA = -1
INVALID_REG = "inv"


SIZE_QUAD_WORD = 8
SIZE_DBL_WORD = 4
SIZE_WORD = 2
SIZE_BYTE = 1

# Indices for the different values in the IfNode children
IDX_IF_NODE_COND = 0
IDX_IF_NODE_THEN = 1
IDX_IF_NODE_ELSE = 2

# The values for the condition to op code mapper
MAP_CND_CD_GT_INT = 0
MAP_CND_CD_GE_INT = 1
MAP_CND_CD_LT_INT = 2
MAP_CND_CD_LE_INT = 3
MAP_CND_CD_EQ_INT = 4
MAP_CND_CD_NE_INT = 5
MAP_CND_CD_GT_FLOAT = 6
MAP_CND_CD_GE_FLOAT = 7
MAP_CND_CD_LT_FLOAT = 8
MAP_CND_CD_LE_FLOAT = 9
MAP_CND_CD_EQ_FLOAT = 10
MAP_CND_CD_NE_FLOAT = 11

# Map DataType to its correspondig size:
map_dt_to_size = {
    DT_INT: DT_SIZE_INT,
    DT_FLOAT: DT_SIZE_FLOAT
}




from abc import ABC, abstractclassmethod
# from multipledispatch import dispatch


class Visitor(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def visit():
        pass



# Super Class for all ASTNode
class ASTNode(ABC):
    def __init__(self) -> None:
        self.node_type = None

        # For the datatype of the nodes:
        self.datatype_original = DT_NONE
        self.datatype_converted = DT_NONE

    @abstractclassmethod
    def accept(visitor: Visitor):
        pass
    

    
# Super Cass for all LeafNode meaning icon, fcon, id and so on.
# It inherits from the ASTNode
class LeafNode(ASTNode):
    def __init__(self) -> None:
        super().__init__()

    def accept(self, visitor: Visitor):
        return visitor.visit(self)

# The Constant Nodes (inherits from LeafNode)
class IConNode(LeafNode):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        self.node_type = "icon"
    
class CConNode(LeafNode):
    def __init__(self, value) -> None:
        super().__init__()
        # the value comes as: 'x', so we are getting just the 2nd index = x
        self.value = value[1]
        self.node_type = "ccon"
    
class FConNode(LeafNode):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        self.node_type = "fcon"


# String Node
class StrNode(LeafNode):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value.strip("\"")
        self.node_type = "str"
        self.str_cons_count = -1
# Type Node
class TypeNode(LeafNode):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        self.node_type = "type"

# VarDef Node
class VarDefNode(LeafNode):
    def __init__(self, id) -> None:
        super().__init__()
        self.value = id
        self.node_type = "vardef"

# VarRef Node
class VarRefNode(LeafNode):
    def __init__(self, id) -> None:
        super().__init__()
        self.value = id
        self.node_type = "varref"

        self.dimension_original = []
        self.dimension_converted = []


# Super Classes for nodes with children

# Unary Node - Super Class for all nodes that has only one child 
# Inherits from ASTNode
class UnaryNode(ASTNode):
    def __init__(self, only_child) -> None:
        super().__init__()
        self.only_child = only_child
    
    def accept(self, visitor:Visitor):
        return visitor.visit(self)
    
    def getOnlyChild(self):
        return self.only_child

# Binary Node - Super Class for all nodes that has two child 
# Inherits from ASTNode
class BinaryNode(ASTNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__()
        self.left_child = left_child
        self.right_child = right_child

    def getLeftChild(self):
        return self.left_child
    
    def getRightChild(self):
        return self.right_child
    
    def accept(self, visitor: Visitor):
        return visitor.visit(self)

# Arthmatic Operation (All derrived from Binary Node)
class AddNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "add"
    
class SubNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "sub"
    
class MulNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "mul"
    
class DivNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "div"


# Logical Operation And and Or is derrived from BinaryNode
class AndNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "and"

class OrNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "or"
    
# Not node is derived from unary node
class NotNode(UnaryNode):
    def __init__(self, only_child) -> None:
        super().__init__(only_child)
        self.node_type = "not"

class EqNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "eq"
    
class NeNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "ne"

class LeNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "le"

class LtNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "lt"

class GeNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "ge"

class GtNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "gt"

# Other Binary Nodes
class VarDecNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "vdecl"

class AssignNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "assign"

class WhileNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "while"

class PDeclNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "pdecl"

class ProgNode(BinaryNode):
    def __init__(self, left_child: ASTNode, right_child: ASTNode) -> None:
        super().__init__(left_child, right_child)
        self.node_type = "prog"

# Other Unary Nodes
class ArrayDefNode(UnaryNode):
    def __init__(self, id, only_child) -> None:
        super().__init__(only_child)
        self.value = id
        self.node_type = "arraydef"


class ArrayRefNode(UnaryNode):
    def __init__(self, id, only_child) -> None:
        super().__init__(only_child)
        self.value = id
        self.node_type = "arrayref"
        

# class IDNode(UnaryNode):
class IdentNode(UnaryNode):
    def __init__(self, id, only_child) -> None:
        super().__init__(only_child)
        self.value = id
        self.node_type = "ident"
        
        # These will store the array info if the ident becomes an array ident
        # They are a list of two items: [IndexType: DT_INT/DT_CHAR, IndexBound]
        # If type is DT_CHAR, the IndexBound should be preconverted from char to int before storing.
        self.dimension_original = []
        self.dimension_converted = []

class ReadNode(UnaryNode):
    def __init__(self, only_child) -> None:
        super().__init__(only_child)
        self.node_type = "read"

class WriteNode(UnaryNode):
    def __init__(self, only_child) -> None:
        super().__init__(only_child)
        self.node_type = "write"

class RetNode(UnaryNode):
    def __init__(self, only_child) -> None:
        super().__init__(only_child)
        self.node_type = "ret"

class FCallNode(UnaryNode):
    def __init__(self, id, only_child) -> None:
        super().__init__(only_child)
        self.value = id
        self.node_type = "fcall"

class PCallNode(UnaryNode):
    def __init__(self, id, only_child) -> None:
        super().__init__(only_child)
        self.value = id
        self.node_type = "pcall"



# Super Class for more than two children (lists)
class MultiChildNode(ASTNode):
    def __init__(self) -> None:
        super().__init__()
        self.children = []

    def accept(self, visitor:Visitor):
        return visitor.visit(self)

class IlistNode(MultiChildNode):
    def __init__(self, id) -> None:
        super().__init__()
        self.children = [id]
        self.node_type = "ilist"
    
    def appendChild(self, id):      
        self.children.append(id)

class VarListNode(MultiChildNode):
    def __init__(self, id) -> None:
        super().__init__()
        if id is not None:
            self.children = [id]
        else:
            self.children = []
        self.node_type = "vlist"
    
    def appendChild(self, id):      
        self.children.append(id)

class ElistNode(MultiChildNode):
    
    def __init__(self) -> None:
        super().__init__()
        self.children = []
        self.node_type = "elist"

    def appendChild(self, expr):
        if expr is not None:
            self.children.append(expr)

class PlistNode(MultiChildNode):
    def __init__(self) -> None:
        super().__init__()
        self.children = []
        self.node_type = "plist"
    
    def appendChild(self, pdecl):
        if pdecl is not None:
            self.children.append(pdecl)
        
class FDeclNode(MultiChildNode):
    def __init__(self) -> None:
        super().__init__()
        self.children = []
        self.node_type = "fdecl"
        self.properties = {
            "type": TypeNode(""),
            "id": "",
            "plist": PlistNode(),
            "vlist": VarListNode(None),
            "stmts": CmpdNode()
        }

        self.children.append(self.properties["type"])
        self.children.append(self.properties["id"])
        self.children.append(self.properties["plist"])
        self.children.append(self.properties["vlist"])
        self.children.append(self.properties["stmts"])

    
    def appendChild(self, type, id, plist, vlist, stmts):
        if type is not None:
            self.properties["type"] = type
            self.children[0] = type
        if id is not None:
            self.properties["id"] = id
            self.children[1] = id
        if plist is not None:
            self.properties["plist"] = plist
            self.children[2] = plist
        if vlist is not None:
            self.properties["vlist"] = vlist
            self.children[3] = vlist
        if stmts is not None:
            self.properties["stmts"] = stmts
            self.children[4] = stmts
        

        

class FlistNode(MultiChildNode):
    def __init__(self) -> None:
        super().__init__()
        self.children = []
        self.node_type = "flist"

    def appendChild(self, fdecl):
        if fdecl is not None:
            self.children.append(fdecl)



class IfNode(MultiChildNode):
    def __init__(self) -> None:
        super().__init__()
        self.children = []
        self.node_type = "if"

    def appendChild(self, test, thn, els):
        self.children.append(test)
        self.children.append(thn)
        if els is not None:
            self.children.append(els)

class CmpdNode(MultiChildNode):
    def __init__(self) -> None:
        super().__init__()
        self.children = []
        self.node_type = "cmpd"

    def appendChild(self, stmt):
        if stmt is not None:
            self.children.append(stmt)


class ExitNode(ASTNode):
    def __init__(self) -> None:
        super().__init__()
        self.node_type = "exit"

    def accept(self, visitor:Visitor):
        return visitor.visit(self)


# Visitor Funcitons

# Visitor Function Class for Type_Checking
# Visit Method:
#   Takes a Node:
#   Evaluates the expression of the node by walking through the tree recursively
#   Adds the datatype_original, and datatype_converted to the node.
#   
#   Parameter: 
#       node - an ASTNode 
#       datataype - an integer value that represensts a datatype [Use the Global constants for better readability]
#



class TypeCheckingVisitor(Visitor):
    def __init__(self):
        # This variable is used to pass info to the next recursive visit
        self.current_dtype = None

        self.dtmap = {
            "int": DT_INT,
            "float": DT_FLOAT,
            "char": DT_CHAR,
            "void": DT_VOID,
            "str": DT_STR
        }

        # Coersion Table (Determines the converted type)
        # It's an array of object
        # Each object represents a table for one or more functions
        # For each object:
        #   The key is "Operand1 & Operand2"
        #   The value is what the Operand1's converted type will be

        self.coersion_table = [
            # (Index: 0) Add, Sub, Mul, Div Coersion Table
            {
                f"{DT_INT}&{DT_INT}": DT_INT,
                f"{DT_INT}&{DT_FLOAT}": DT_FLOAT,
                f"{DT_FLOAT}&{DT_FLOAT}": DT_FLOAT,
                f"{DT_CHAR}&{DT_CHAR}": DT_CHAR,
                f"{DT_CHAR}&{DT_INT}": DT_INT,
                f"{DT_CHAR}&{DT_FLOAT}": ERROR_ARITH

            },

            #(Index: 1) AND, OR Table
            {
                f"{DT_INT}&{DT_INT}": DT_INT,
                f"{DT_INT}&{DT_FLOAT}": DT_INT,
                f"{DT_FLOAT}&{DT_FLOAT}": DT_INT,
                f"{DT_CHAR}&{DT_CHAR}": DT_INT,
                f"{DT_CHAR}&{DT_INT}": ERROR_BOOL,
                f"{DT_CHAR}&{DT_FLOAT}": ERROR_BOOL
            },

            #(Index: 2) Relational Operations (GT,GTE, LT,LTE, EQ, NEQ)
            {
                f"{DT_INT}&{DT_INT}": DT_INT,
                f"{DT_INT}&{DT_FLOAT}": DT_INT,
                f"{DT_FLOAT}&{DT_FLOAT}": DT_INT,
                f"{DT_CHAR}&{DT_CHAR}": DT_INT,
                f"{DT_CHAR}&{DT_INT}": ERROR_CMP,
                f"{DT_CHAR}&{DT_FLOAT}": ERROR_CMP
            }

        ]

        # The first object will be used for function names, the second object will be used for global variable
        # We will append an object for each new function we encounter.
        self.stack = [dict(), {"vdecl": dict()}]

    def visit(self, node):
        if isinstance(node, ProgNode):
            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE
            
            # Processing $vlist
            node.getLeftChild().accept(self)

            # processing $flist
            node.getRightChild().accept(self)


            # Now we need to check if all Global variables is referenced or not
            for vdecl_info in self.stack[INDEX_STACK_GLOBALS]["vdecl"].values():
                if not vdecl_info[INDEX_ST_FR_VDECL_IS_REFERENCED]:
                    vdecl_info[INDEX_ST_FR_VDECL_POINTER].datatype_original = ERROR_UNR
                    vdecl_info[INDEX_ST_FR_VDECL_POINTER].datatype_converted = DT_NONE
            
        elif isinstance(node, VarListNode) or isinstance(node, FlistNode):
            # Processing all vdecl/fdecl nodes
            for child in node.children:
                child.accept(self)

            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE
            
        elif isinstance(node, VarDecNode):
            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE

            # Processing Type Node
            self.current_dtype = node.getLeftChild().accept(self)[0]

            # Processing Ilist Node
            node.getRightChild().accept(self)

        elif isinstance(node, TypeNode):
            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE

            return [self.dtmap[node.value]]

        elif isinstance(node, IlistNode):
            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE

            for ident in node.children:
                ident.accept(self)

        elif isinstance(node, FDeclNode):
            # Global variables
            # The new function datatype will be assigned the number represented by DT_FUNCTION_COUNTER. We will then increment it.
            global DT_FUNCTION_COUNTER
            global map_dtToPrint
            global function_dt_mapper


            # Add a stack frame on the Stack for the new procedure
            # Each stack frame will have vdecl (dict), and vreffed(map)
            # The vdecl list will contain all the id that was declared (which will be used to check if a variable was declared or not)
            # The vreffed list will contain all the id that was reffenced through vdef or vref atleast once. (will be used to check for unreferenced variables)
            stack_frame = {"vdecl":dict(), "vreffed": set(), "func_name": node.properties["id"]}
            self.stack.append(stack_frame)

            # Processing the Type, and storing the the function return type
            node.properties["type"].accept(self)

            function_return_type = self.dtmap[node.properties["type"].value]


            # Processing the PlistNode.

            # The parameter_type_list is something like this: 
            #   [[1, 1, 10], 1, 2] or [[DT_INT, DT_CHAR, 99], DT_INT, DT_FLOAT]
            # Note: For regular type we add just the value, but for a array we add a list of three items:
            # 1. DataType of parameter - INDEX_PLIST_ARA_PR_DT
            # 2. DataType of Index - INDEX_PLIST_ARA_IND_DT
            # 3. IndexBound - INDEX_PLIST_ARA_IND_BND

            parameter_type_list = []
            node.properties["plist"].accept(self)
            for pdecl_node in node.properties["plist"].children:
                parameter_type = self.dtmap[pdecl_node.getLeftChild().value]
                ident_node = pdecl_node.getRightChild()
                if len(ident_node.dimension_original) == 0:
                    # The ident is NOT an array
                    parameter_type_list.append(parameter_type)
                else:
                    # The ident is an array
                    # Insert a list: [Para_DT, Ind_DT, Ind_BND]
                    parameter_type_list.append([parameter_type, 
                                                ident_node.dimension_original[INDEX_DIM_ARA_IDENT_TYPE], 
                                                ident_node.dimension_original[INDEX_DIM_ARA_IDENT_BOUND]])



            # Process VList
            node.properties["vlist"].accept(self)

            
            # We have to check if the function 
            # was already defined as another function or a global variable.
            function_name = node.properties["id"]
            if function_name in self.stack[INDEX_STACK_FUNCTIONS] or function_name in self.stack[INDEX_STACK_GLOBALS]["vdecl"]:
                node.datatype_original = ERROR_DMUL
                node.datatype_converted = DT_NONE

                # Pushing to the stack as an error
                self.stack[INDEX_STACK_FUNCTIONS][function_name] = [ERROR_DMUL, ERROR_DMUL, False]
            else:
                # Valid Function Name
                # We will create a new data type for the funciton before processing the body, because the function can call itself.
                # Constructing the string for the new function datatype
                # Example of ftype_str = int&float->float
                # Example of ftype_IR = 1&2->2
                ftype_str = ""
                ftype_IR = ""

                for i in range(len(parameter_type_list)):
                    if i != 0:
                        ftype_str += "&"
                        ftype_IR += "&"
                    
                    if isinstance(parameter_type_list[i], list):
                        # If item is a list then it's an array
                        # Add Datatype
                        ftype_str += map_dtToPrint[parameter_type_list[i][INDEX_PLIST_ARA_PR_DT]]
                        ftype_IR += str(parameter_type_list[i][INDEX_PLIST_ARA_PR_DT])

                        # Add the bound
                        ftype_str += "[" + str(parameter_type_list[i][INDEX_PLIST_ARA_IND_BND]) + "]"
                        ftype_IR  += "[" + str(parameter_type_list[i][INDEX_PLIST_ARA_IND_BND]) + "]"
                    else:
                        ftype_str += map_dtToPrint[parameter_type_list[i]]
                        ftype_IR += str(parameter_type_list[i])
                
                ftype_str += "->" + map_dtToPrint[function_return_type]
                ftype_IR += "->" + str(function_return_type)

                # Check if this function datatype already exists
                if ftype_IR in function_dt_mapper:
                    function_datatype = function_dt_mapper[ftype_IR]
                else:
                    # Set function datatype value to the current function counter 
                    function_datatype = DT_FUNCTION_COUNTER
                    
                    # add function datattype the function_dtype_mapper
                    map_dtToPrint[function_datatype] = ftype_str
                    function_dt_mapper[ftype_IR] = function_datatype
                    DT_FUNCTION_COUNTER += 1


                
                # Adding the Function Datatype to the map using the function counter. 
                node.datatype_original = function_datatype
                node.datatype_converted = function_datatype

                # Add function name and dtype to the stack, 
                # The function stack will accept a list of three items for a function:
                # 1. Function's Return Datatype
                # 2. Functions's own data type -> DT_FUNCTION_COUNTER
                # 3. hasReturned -> True/False
                self.stack[INDEX_STACK_FUNCTIONS][function_name] = [function_return_type, function_datatype, False]
                

                # Increment the Counter to keep it ready for next use.
                DT_FUNCTION_COUNTER += 1


            # Process Body (Compound Stmt)
            node.properties["stmts"].accept(self)
            
            # (Method DEPRECATED) Check all declared variables are defined/referenced
            # vdecl_id_set = set(self.stack[-1]["vdecl"].keys())
            # vreffed_id_set = self.stack[-1]["vreffed"]

            # if vdecl_id_set != vreffed_id_set:
            #     # All of vdecl id is not present in the vreffed
            #     # Getting the ones that are not reffed:
            #     not_referenced = vdecl_id_set - vreffed_id_set

            #     # Setting original type of those idents to error_unr
            #     for id in not_referenced:
            #         ident_node = self.stack[-1]["vdecl"][id][INDEX_ST_FR_VDECL_POINTER]
            #         ident_node.datatype_original = ERROR_UNR 

            # Check all declared variables are defined/referenced
            for vdecl_info in self.stack[-1]["vdecl"].values():
                if not vdecl_info[INDEX_ST_FR_VDECL_IS_REFERENCED]:
                    vdecl_info[INDEX_ST_FR_VDECL_POINTER].datatype_original = ERROR_UNR
                    vdecl_info[INDEX_ST_FR_VDECL_POINTER].datatype_converted = DT_NONE


            
            hasReturned = self.stack[INDEX_STACK_FUNCTIONS][function_name][INDEX_STACK_FUNCTIONS_HAS_RETURNED]    

            # Checking if there is a return statement
            if not hasReturned:
                if function_return_type != DT_VOID:
                    # Function didn't return, and the return type is not void. So raise error
                    node.datatype_original = ERROR_NRT
                    node.datatype_converted = DT_NONE
            else:
                if function_return_type == DT_VOID:
                    # Void Function has a return statement
                    node.datatype_original = ERROR_VRT
                    node.datatype_converted = DT_NONE


            self.stack.pop()
            
        elif isinstance(node, RetNode):
            function_name = self.stack[-1]["func_name"]
            function_return_type = self.stack[INDEX_STACK_FUNCTIONS][function_name][INDEX_STACK_FUNCTIONS_RETURN]

            child_of_ret = node.getOnlyChild()
            child_of_ret.accept(self)
            if child_of_ret.datatype_converted != function_return_type:
                # The return type of the statement doesn't match the return type of the of the function
                # Setting the original type of return statement to err_rtt
                node.datatype_original = ERROR_RTT
            else:
                node.datatype_original = DT_NONE

            node.datatype_converted = DT_NONE

            # Setting Function's hasReturned value to True:
            self.stack[INDEX_STACK_FUNCTIONS][function_name][INDEX_STACK_FUNCTIONS_HAS_RETURNED] = True



        elif isinstance(node, FCallNode):
            # Processing the Elist (Expression for arguement list)
            # arg_type_list = node.getOnlyChild().accept(self)

            node.getOnlyChild().accept(self)

            # Store all the argument types in a list
            # The format of the list will be: Each item will be either a integer value or a list.
            # If an argument is not an array, it will only have Integere Dtype value of the type. Ex: DT_INT, DT_FLOAT
            # If an argument is an array, it will have a list item, containing the type of the array and the dimesion. Ex: [DT_INT, 20]
            # A complete example:
            #  For an argument list: (int x, char y, float z[10]) -> [DT_INT, DT_CHAR, [DT_FLOAT, 10]]
            arg_type_list = []

            for arg in node.getOnlyChild().children:
                # We will get the argument types from the stack. NOT from the node
                # Because, the varref node might set a node to error_dim if it sees a varref call to an array node
                # We know that during Function and Procedure call, the array nodes are passed without the dimensions
                # meaning A[20] is passed as A

                if isinstance(arg, VarRefNode):
                    arg_name = arg.value

                    found = False
                    if arg_name in self.stack[-1]["vdecl"]:
                        # Present in Local Stack
                        vdecl_info_of_arg = self.stack[-1]["vdecl"][arg_name]
                        found = True

                    elif arg_name in self.stack[INDEX_STACK_GLOBALS]["vdecl"]:
                        # Present in Global Stack
                        vdecl_info_of_arg = self.stack[INDEX_STACK_GLOBALS]["vdecl"][arg_name]
                        found = True
                    else:
                        # Not Present.
                        # Setting it to whatever will be set by the visiting the arg node.
                        arg_type = arg.datatype_converted
                        arg_type_list.append(arg_type)

                    if found:
                        arg_type = vdecl_info_of_arg[INDEX_ST_FR_VDECL_TYPE]
                        if arg_type == DT_ARRAY_INT or arg_type == DT_ARRAY_FLOAT or arg_type == DT_ARRAY_CHAR:
                            # It's an array, so we need to store the dimension too.
                            dimension = vdecl_info_of_arg[INDEX_ST_FR_VDECL_POINTER].dimension_original[INDEX_DIM_ARA_IDENT_BOUND]
                            
                            arg_type_list.append([arrayDTtoRegDT(arg_type), dimension])
                            
                            # Since this is valid, we also have to set the varref node to valid as well.
                            # Remember that it was set to error_dim, due to arraynode being visited as varref node.
                            arg.datatype_original = arg_type
                            arg.datatype_converted = arg_type

                            arg.dimension_original.append(arrayDTtoRegDT(arg_type))
                            arg.dimension_original.append(dimension)

                            arg.dimension_converted.append(arrayDTtoRegDT(arg_type))
                            arg.dimension_converted.append(dimension)


                        else:
                            arg_type_list.append(arg_type)

                else:
                    # arg is an expression
                    arg_type = arg.datatype_converted
                    
                    arg_type_list.append(arg_type)

            # Check if a variable is being called as a function
            if node.value in self.stack[-1]["vdecl"]:
                node.datatype_original = ERROR_NFN
                node.datatype_converted = DT_NONE

                # Updating the vdecl isReferenced to True
                # self.stack[-1]["vreffed"].add(node.value)
                self.stack[1]["vdecl"][node.value][INDEX_ST_FR_VDECL_IS_REFERENCED] = True

            elif node.value in self.stack[INDEX_STACK_GLOBALS]["vdecl"]:
                node.datatype_original = ERROR_NFN
                node.datatype_converted = DT_NONE

            # Check if the function is declared or not
            elif node.value not in self.stack[INDEX_STACK_FUNCTIONS]:
                node.datatype_original = ERROR_NFN
                node.datatype_converted = DT_NONE
            else:
                # Getting the Return Type of the Declared Fcall
                fdecl_return_type = self.stack[INDEX_STACK_FUNCTIONS][node.value][INDEX_STACK_FUNCTIONS_RETURN]

                # If the return type is void, then this shouldn't be a fcall, it's supposed to be a pcall
                if fdecl_return_type == DT_VOID:
                    node.datatype_original = ERROR_FNP
                    node.datatype_converted = DT_NONE
                else:
                    # Construct the data type IR of the fcall
                    fcalltype_IR = ""
                    for i, arg_type in enumerate(arg_type_list):
                        if i != 0:
                            fcalltype_IR += "&"
                        if isinstance(arg_type, list):
                            # It's an array.
                            # The first item of the list is the array type, and the second is the dimension
                            fcalltype_IR += str(arg_type[0]) + "[" + str(arg_type[1]) +"]"
                        else:
                            fcalltype_IR += str(arg_type)

                    
                    fcalltype_IR += "->" + str(fdecl_return_type)

                    # Get the integer value of the fcalltype IR
                    if fcalltype_IR not in function_dt_mapper:
                        # Data Type not found = Param Argument mismatch
                        node.datatype_original = ERROR_PRM
                        node.datatype_converted = DT_NONE
                    else:
                        fcalltype = function_dt_mapper[fcalltype_IR]
                        fdecltype = self.stack[INDEX_STACK_FUNCTIONS][node.value][INDEX_STACK_FUNCTIONS_DTYPE]

                        # Check if the fcalltype matches the fdecltype
                        if fcalltype != fdecltype:
                            node.datatype_original = ERROR_PRM
                            node.datatype_converted = DT_NONE
                        else:
                            node.datatype_original = fdecl_return_type
                            node.datatype_converted = fdecl_return_type
            
                
        
        elif isinstance(node, ElistNode):
            arg_type_list = []
            # Process all Expressions
            for exp_node in node.children:
                exp_node.accept(self)
                arg_type_list.append(exp_node.datatype_converted)

            return arg_type_list
        
        


        elif isinstance(node, PlistNode):
            
            # Processing the list of Pdecl node.
            # Each of the Pdecl node will return their type of the parameter.
            # We will store those in a list.
            pdecl_types = []
            for pdecl in node.children:
                pdecl_types.append(pdecl.accept(self)[0])

            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE

            return pdecl_types

        elif isinstance(node, PDeclNode):
            
            # Process the typenode
            pdecl_type = node.getLeftChild().accept(self)[0]
            
            # The IdentNode needs the type
            self.current_dtype = pdecl_type

            node.getRightChild().accept(self)

            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE

            return [pdecl_type]

        elif isinstance(node, PCallNode):
            # Process the argument list
            node.getOnlyChild().accept(self)

            # Store all the argument types in a list
            # The format of the list will be: Each item will be either a integer value or a list.
            # If an argument is not an array, it will only have Integere Dtype value of the type. Ex: DT_INT, DT_FLOAT
            # If an argument is an array, it will have a list item, containing the type of the array and the dimesion. Ex: [DT_INT, 20]
            # A complete example:
            #  For an argument list: (int x, char y, float z[10]) -> [DT_INT, DT_CHAR, [DT_FLOAT, 10]]
            arg_type_list = []

            for arg in node.getOnlyChild().children:
                # We will get the argument types from the stack. NOT from the node
                # Because, the varref node might set a node to error_dim if it sees a varref call to an array node
                # We know that during Function and Procedure call, the array nodes are passed without the dimensions
                # meaning A[20] is passed as A

                if isinstance(arg, VarRefNode):
                    arg_name = arg.value

                    found = False
                    if arg_name in self.stack[-1]["vdecl"]:
                        # Present in Local Stack
                        vdecl_info_of_arg = self.stack[-1]["vdecl"][arg_name]
                        found = True

                    elif arg_name in self.stack[INDEX_STACK_GLOBALS]["vdecl"]:
                        # Present in Global Stack
                        vdecl_info_of_arg = self.stack[INDEX_STACK_GLOBALS]["vdecl"][arg_name]
                        found = True
                    else:
                        # Not Present.
                        # Setting it to whatever will be set by the visiting the arg node.
                        arg_type = arg.datatype_converted
                        arg_type_list.append(arg_type)

                    if found:
                        arg_type = vdecl_info_of_arg[INDEX_ST_FR_VDECL_TYPE]
                        if arg_type == DT_ARRAY_INT or arg_type == DT_ARRAY_FLOAT or arg_type == DT_ARRAY_CHAR:
                            # It's an array, so we need to store the dimension too.
                            dimension = vdecl_info_of_arg[INDEX_ST_FR_VDECL_POINTER].dimension_original[INDEX_DIM_ARA_IDENT_BOUND]
                            
                            arg_type_list.append([arrayDTtoRegDT(arg_type), dimension])
                            
                            # Since this is valid, we also have to set the varref node to valid as well.
                            # Remember that it was set to error_dim, due to arraynode being visited as varref node.
                            arg.datatype_original = arg_type
                            arg.datatype_converted = arg_type

                            arg.dimension_original.append(arrayDTtoRegDT(arg_type))
                            arg.dimension_original.append(dimension)

                            arg.dimension_converted.append(arrayDTtoRegDT(arg_type))
                            arg.dimension_converted.append(dimension)


                        else:
                            arg_type_list.append(arg_type)

                else:
                    # arg is an expression
                    arg_type = arg.datatype_converted
                    
                    arg_type_list.append(arg_type)


            # Check if a variable is being called as a procedure
            if node.value in self.stack[-1]["vdecl"]:
                node.datatype_original = ERROR_NPR
                node.datatype_converted = DT_NONE

                # Updating the vdecl isReferenced to True

                # self.stack[-1]["vreffed"].add(node.value)
                self.stack[1]["vdecl"][node.value][INDEX_ST_FR_VDECL_IS_REFERENCED] = True
            
            elif node.value in self.stack[INDEX_STACK_GLOBALS]:
                # Check Globals 
                node.datatype_original = ERROR_NPR
                node.datatype_converted = DT_NONE

            # Check if the procedure is declared or not
            elif node.value not in self.stack[INDEX_STACK_FUNCTIONS]:
                node.datatype_original = ERROR_NPR
                node.datatype_converted = DT_NONE
            else:
                # Getting the Return Type of the Declared Fcall
                pdecl_return_type = self.stack[INDEX_STACK_FUNCTIONS][node.value][INDEX_STACK_FUNCTIONS_RETURN]

                # If the return type is note void, then this shouldn't be a pcall, it's supposed to be an fcall
                if pdecl_return_type != DT_VOID:
                    node.datatype_original = ERROR_PRF
                    node.datatype_converted = DT_NONE
                else:
                    # Construct the data type IR of the fpcall
                    pcalltype_IR = ""
                    for i, arg_type in enumerate(arg_type_list):
                        if i != 0:
                            pcalltype_IR += "&"
                        pcalltype_IR += str(arg_type)


                    
                    pcalltype_IR += "->" + str(pdecl_return_type)

                    # Get the actual pcalltype IR
                    if pcalltype_IR not in function_dt_mapper:
                        # Data Type not found = Param Argument mismatch
                        node.datatype_original = ERROR_PRM
                        node.datatype_converted = DT_NONE
                    else:
                        pcalltype = function_dt_mapper[pcalltype_IR]
                        pdecltype = self.stack[INDEX_STACK_FUNCTIONS][node.value][INDEX_STACK_FUNCTIONS_DTYPE]

                        # Check if the pcalltype matches the pdecltype
                        if pcalltype != pdecltype:
                            node.datatype_original = ERROR_PRM
                            node.datatype_converted = DT_NONE
                        else:
                            node.datatype_original = pdecl_return_type
                            node.datatype_converted = pdecl_return_type
        
        elif isinstance(node, IdentNode):
            # Checking if the ident already has been declared in the current stack frame
            if node.value in self.stack[-1]["vdecl"]:
                node.datatype_original = ERROR_DMUL
                # node.datatype_converted = self.stack[-1]["vdecl"][node.value][INDEX_ST_FR_VDECL_TYPE]
                node.datatype_converted = DT_NONE
            else:
                node.datatype_original = self.current_dtype
                node.datatype_converted = self.current_dtype

                # We have to process the dimension here
                con_node = node.getOnlyChild()
                if con_node is not None:
                    con_node.accept(self)

                    # Changing the Data type to an array data type
                    if node.datatype_original == DT_INT:
                        node.datatype_original = DT_ARRAY_INT
                        node.datatype_converted = DT_ARRAY_INT
                    elif node.datatype_original == DT_FLOAT:
                        node.datatype_original = DT_ARRAY_FLOAT
                        node.datatype_converted = DT_ARRAY_FLOAT
                    elif node.datatype_original == DT_CHAR:
                        node.datatype_original = DT_ARRAY_CHAR
                        node.datatype_converted = DT_ARRAY_CHAR
                    
                    # Adding the dimension info of the array to the IDentNode
                    if isinstance(con_node, IConNode):
                        node.dimension_original = [DT_INT, con_node.value]
                        node.dimension_converted = [DT_INT, con_node.value]
                    elif isinstance(con_node, CConNode):
                        index = con_node.value

                        index_bound = charToInt(index)
                        if index_bound == -1:
                            node.datatype_original = ERROR_SUB
                            node.datatype_converted = DT_NONE
                        else:
                            node.dimension_original = [DT_CHAR, index_bound]
                            node.dimension_converted = [DT_CHAR, index_bound]

                    elif isinstance(con_node, FConNode):
                        # The dimension cannot be float, so, it will be a error_sub
                        node.datatype_original = ERROR_SUB
                        node.datatype_converted = DT_NONE

                # Push it on the stack frame in the vdecl ooject. 
                # Each variable entity is a list of three items [TYPE, POINTER_TO_VDECL_ASTNODE, Is_Referenced=False]
                # The key is the string <ID> itself
                self.stack[-1]["vdecl"][node.value] = [node.datatype_original, node, False]

        elif isinstance(node, IConNode):
            node.datatype_original = DT_INT
            node.datatype_converted = DT_INT

        elif isinstance(node, FConNode):
            node.datatype_original = DT_FLOAT
            node.datatype_converted = DT_FLOAT
        
        elif isinstance(node, CConNode):
            node.datatype_original = DT_CHAR
            node.datatype_converted = DT_CHAR


        elif isinstance(node, VarDefNode) or isinstance(node, VarRefNode):
            # Check if the variable is declared or not by looking at the current stack-frame or the global variables
            # Check Current Stack Frame.
            # The current stack frame is located at the last position of the stack, hence the use of -1 index
            if node.value not in self.stack[-1]["vdecl"]:
                # Check Global Variables
                if node.value not in self.stack[INDEX_STACK_GLOBALS]["vdecl"]:
                    # Not present at all
                    node.datatype_original = ERROR_UND
                    node.datatype_converted = DT_NONE

                    return
                else:
                    # Present in Global
                    self.stack[INDEX_STACK_GLOBALS]["vdecl"][node.value][INDEX_ST_FR_VDECL_IS_REFERENCED] = True
                    var_datatype = self.stack[INDEX_STACK_GLOBALS]["vdecl"][node.value][INDEX_ST_FR_VDECL_TYPE]

            else:
                # Present in the current Stack Frame
                # Change isRefenced to True to indicate that this variable has been referenced
                self.stack[-1]["vdecl"][node.value][INDEX_ST_FR_VDECL_IS_REFERENCED] = True
                var_datatype = self.stack[-1]["vdecl"][node.value][INDEX_ST_FR_VDECL_TYPE]

            if var_datatype == DT_ARRAY_INT or \
                var_datatype == DT_ARRAY_FLOAT or \
                var_datatype == DT_ARRAY_CHAR:
                # The datatype is an array, but it is being referenced as a varref/vardef
                node.datatype_original = ERROR_DIM
                node.datatype_converted = DT_NONE
            else:
                # Correct Datatype
                node.datatype_original = var_datatype 
                node.datatype_converted = var_datatype


                


            # This return is not needed by vardef, we are only using it for varref
            return [node.datatype_converted]

        elif isinstance(node, ArrayDefNode) or isinstance(node, ArrayRefNode):
            node.getOnlyChild().accept(self)
            if node.value not in self.stack[-1]["vdecl"]:
                if node.value not in self.stack[INDEX_STACK_GLOBALS]["vdecl"]:
                    # Not present, so error undefined
                    node.datatype_original = ERROR_UND
                    node.datatype_converted = DT_NONE
                    return
                else:
                    # Present in Global Stack
                    vdecl_type = self.stack[INDEX_STACK_GLOBALS]["vdecl"][node.value][INDEX_ST_FR_VDECL_TYPE]
                    vdecl_node = self.stack[INDEX_STACK_GLOBALS]["vdecl"][node.value][INDEX_ST_FR_VDECL_POINTER]

                    # change isRefenced to True to indicate that this variable has been referenced
                    self.stack[INDEX_STACK_GLOBALS]["vdecl"][node.value][INDEX_ST_FR_VDECL_IS_REFERENCED] = True
            else:
                # We found a vdecl name match in the local stack frame
                vdecl_type = self.stack[-1]["vdecl"][node.value][INDEX_ST_FR_VDECL_TYPE]
                vdecl_node = self.stack[-1]["vdecl"][node.value][INDEX_ST_FR_VDECL_POINTER]

                # (DEPRECATED) Put it on the stack frame for the vreffed as this has been used in vdef or vref
                # self.stack[-1]["vreffed"].add(node.value)

                # Change isRefenced to True to indicate that this variable has been referenced
                self.stack[-1]["vdecl"][node.value][INDEX_ST_FR_VDECL_IS_REFERENCED] = True


            # Now, type check the node, and the dimensions for arrays
            node.datatype_converted = vdecl_type
            node.datatype_original = vdecl_type

            index_node = node.getOnlyChild()

            # Checking if the found vdecl is an array or not
            if (vdecl_type != DT_ARRAY_INT) and (vdecl_type != DT_ARRAY_FLOAT) and (vdecl_type != DT_ARRAY_CHAR):
                node.datatype_original = ERROR_DIM
                node.datatype_converted = DT_NONE
            else:
                vdecl_index_type = vdecl_node.dimension_original[INDEX_DIM_ARA_IDENT_TYPE]
                vdecl_index_bound = vdecl_node.dimension_original[INDEX_DIM_ARA_IDENT_BOUND]

                # Checking the Type of index
                if isinstance(index_node, IConNode):
                    curr_array_index_bound = index_node.value
                    if vdecl_index_type != DT_INT:
                        # IndexType mismatch (given int, expecting char)
                        node.datatype_original = ERROR_SUB
                        node.datatype_converted = DT_NONE
                    else:
                        if curr_array_index_bound < 0 or curr_array_index_bound >= vdecl_index_bound:
                            # Index outside of bound than defined (bound: 0 to len(bound)-1)
                            node.datatype_original = ERROR_BND
                            node.datatype_converted = DT_NONE

                elif isinstance(index_node, CConNode):
                    curr_array_index_bound = index_node.value
                    # the ccon values are converted to integers for arrays, there converted type is int.
                    index_node.datatype_converted = DT_INT

                    if vdecl_index_type != DT_CHAR:
                        # IndexType mismatch (given char, expecting int)
                        node.datatype_original = ERROR_SUB
                        node.datatype_converted = DT_NONE
                    else:
                        curr_array_index_bound_converted = charToInt(curr_array_index_bound)

                        if curr_array_index_bound_converted > vdecl_index_bound  or \
                            curr_array_index_bound_converted < charToInt('a'):
                            # Index outside of bound than defined
                            node.datatype_original = ERROR_BND
                            node.datatype_converted = DT_NONE

                elif isinstance(index_node, FConNode):
                    node.datatype_original = ERROR_SUB
                    node.datatype_converted = DT_NONE
                
                else:
                    # its an expression of some sort.
                    if index_node.datatype_converted != vdecl_index_type:
                        node.datatype_original = ERROR_SUB
                        node.datatype_converted = DT_NONE
                    else:
                        # The converted type of the index node becomes int at all times.
                        index_node.datatype_converted = DT_INT

        
        elif isinstance(node, AssignNode):
            
            left_child = node.getLeftChild()
            right_child = node.getRightChild()

            left_child.accept(self)
            right_child.accept(self)

            # if the right child is an error, then our left child (vardef) will have a converted_type of 'none'
            # if right_child.datatype_original in ERRORS or right_child.datatype_original == DT_NONE:
            # if right_child.datatype_original in ERRORS:
            #     left_child.datatype_converted = DT_NONE
            # elif left_child.datatype_original in ERRORS:
            if left_child.datatype_original in ERRORS:
                right_child.datatype_converted = DT_NONE
            else:
                if right_child.datatype_original not in ERRORS:
                    # Change Right Operands converted type only if the original type of it is not error
                    right_child.datatype_converted = left_child.datatype_original

            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE


        # Arithmatic Operations
        elif isinstance(node, AddNode) or isinstance(node, SubNode) \
            or isinstance(node, MulNode) or isinstance(node, DivNode):
            op1 = node.getLeftChild()
            op2 = node.getRightChild()

            op1.accept(self)
            op2.accept(self)

            op1_type = arrayDTtoRegDT(op1.datatype_converted)
            op2_type = arrayDTtoRegDT(op2.datatype_converted)


            if op1_type in ERRORS or op2_type in ERRORS:
                node.datatype_original = DT_NONE
                node.datatype_converted = DT_NONE
            else:
                coersion_table = self.coersion_table[INDEX_COERSION_ADD]

                # So basically we are going to check if op1&op2 is available in the coersion table as key, if yes, we will
                # set the converted type of op1 to the coersiontable's value for op1&op2
                # Example:
                #   if we have int&float = float, then
                #   the int will be converted to a float
                # But what if we have op1=float, and op2=int? There is no float&int in the table
                # in that case we will check if "op2&op1" is available as a key. "op2&op1" becomes int&float which is available in the table. 
                # this time we will change the converted type of the op2 instead of op1.
                if f"{op1_type}&{op2_type}" in coersion_table:
                    op1.datatype_converted = coersion_table[f"{op1_type}&{op2_type}"]
                    node.datatype_original = coersion_table[f"{op1_type}&{op2_type}"]
                elif f"{op2_type}&{op1_type}" in coersion_table:
                    op2.datatype_converted = coersion_table[f"{op2_type}&{op1_type}"]
                    node.datatype_original = coersion_table[f"{op2_type}&{op1_type}"]
                else:
                    # Not in the coersion_table, meaning one of the operands is error or none
                    node.datatype_original = DT_NONE


                # Setting the converted type same as original
                node.datatype_converted = node.datatype_original
        
        
        # Logical Operations
        # AND, OR
        elif isinstance(node, AndNode) or isinstance(node, OrNode):
            op1 = node.getLeftChild()
            op2 = node.getRightChild()

            op1.accept(self)
            op2.accept(self)

            op1_type = arrayDTtoRegDT(op1.datatype_converted)
            op2_type = arrayDTtoRegDT(op2.datatype_converted)

            if op1_type in ERRORS or op2_type in ERRORS:
                node.datatype_original = DT_NONE
                node.datatype_converted = DT_NONE
            else:
                coersion_table = self.coersion_table[INDEX_COERSION_AND]

                if f"{op1_type}&{op2_type}" in coersion_table:
                    node.datatype_original = coersion_table[f"{op1_type}&{op2_type}"]
                elif f"{op2_type}&{op1_type}" in coersion_table:
                    node.datatype_original = coersion_table[f"{op2_type}&{op1_type}"]

                if node.datatype_original in ERRORS:
                    node.datatype_converted = DT_NONE
                else:
                    node.datatype_converted = node.datatype_original
                

        # NOT
        elif isinstance(node, NotNode):
            node.getOnlyChild().accept(self)

            if node.only_child.datatype_original in ERRORS:
                node.datatype_original = DT_NONE
            elif node.only_child.datatype_converted != DT_INT:
                node.datatype_original = ERROR_BOOL
                node.datatype_converted = DT_NONE
            else:
                node.datatype_original = DT_INT
                node.datatype_converted = DT_INT



        # Relational Operations (GT, GE, LT, LE, EQ, NE)
        elif isinstance(node, GtNode) or isinstance(node, GeNode) or isinstance(node, LtNode) or \
            isinstance(node, LeNode) or isinstance(node, EqNode) or isinstance(node, NeNode):
            op1 = node.getLeftChild()
            op2 = node.getRightChild()

            op1.accept(self)
            op2.accept(self)

            op1_type = arrayDTtoRegDT(op1.datatype_converted)
            op2_type = arrayDTtoRegDT(op2.datatype_converted)

            if op1_type in ERRORS or op2_type in ERRORS:
                node.datatype_original = DT_NONE
                node.datatype_converted = DT_NONE
            else:
                coersion_table = self.coersion_table[INDEX_COERSION_RELATIONAL]

                if f"{op1_type}&{op2_type}" in coersion_table:
                    node.datatype_original = coersion_table[f"{op1_type}&{op2_type}"]
                    node.datatype_converted = node.datatype_original
                elif f"{op2_type}&{op1_type}" in coersion_table:
                    node.datatype_original = coersion_table[f"{op2_type}&{op1_type}"]
                    node.datatype_converted = node.datatype_original

                # Converting the operand int to float if the other operand is a float
                if op1_type == DT_INT and op2_type == DT_FLOAT:
                    op1.datatype_converted = DT_FLOAT
                elif op1_type == DT_FLOAT and op2_type == DT_INT:
                    op2.datatype_converted = DT_FLOAT

                if node.datatype_original in ERRORS:
                    node.datatype_converted = DT_NONE

        elif isinstance(node, WriteNode) or isinstance(node, ReadNode):
            node.getOnlyChild().accept(self)
            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE

        elif isinstance(node, ExitNode):
            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE

        elif isinstance(node, WhileNode):
            node.getLeftChild().accept(self)
            node.getRightChild().accept(self)

            # The while has a comparison condition on the leftchild, and we know that all relational node produces int.
            # If the leftchild node is not a conditional node,
            # we will set the converted datatype to DT_INT
            left_node = node.getLeftChild()
            if not isConditionalNode(left_node):
                if left_node.datatype_original not in ERRORS:
                    left_node.datatype_converted = DT_INT

            node.datatype_original = DT_NONE
            node.datatype_converted = DT_NONE

        elif isinstance(node, CmpdNode) or isinstance(node, IfNode):
            for stmt in node.children:
                stmt.accept(self)

        elif isinstance(node, StrNode):
            node.datatype_original = DT_STR
            node.datatype_converted = DT_STR



        

            
    
# Utility Functions
# Returns -1 for outofbound
def charToInt(index):
    return ord(index)
    
            
# If the Data Type is in array format: DT_ARRAY_*, then this function returns the base datatype
# Used when we need to compare a base datatype
def arrayDTtoRegDT(datatype:int):
    dataype_mapper = {
        DT_ARRAY_INT: DT_INT,
        DT_ARRAY_FLOAT: DT_FLOAT,
        DT_ARRAY_CHAR: DT_CHAR
    }
    if datatype in dataype_mapper:
        return dataype_mapper[datatype]
    else:
        return datatype


def isConditionalNode(node):
    if isinstance(node, AndNode) or isinstance(node, OrNode) or isinstance(node, NotNode) or \
        isinstance(node, LtNode) or isinstance(node, LeNode) or isinstance(node, GtNode) or \
        isinstance(node, GeNode) or isinstance(node, EqNode) or isinstance(node, NeNode):
        return True
    else:
        return False


# Visitor Function class for print
class PrintVisitor(Visitor):
    def visit(self, node):
        global map_dtToPrint
    
        if isinstance(node, LeafNode):
            result = "#($"
            result += node.node_type 

            # Data Type Add
            result += ":" + map_dtToPrint[node.datatype_original] 
            
            
            if isinstance(node, VarRefNode):
                # If the datatype is an array (for function and procedure calls, arrays are passed as varref)
                if node.datatype_original == DT_ARRAY_INT \
                    or node.datatype_original == DT_ARRAY_FLOAT \
                    or node.datatype_original == DT_ARRAY_CHAR:

                    dimension = node.dimension_original[1]                    

                    result += "[" + str(dimension) + "]"
            
            result += ":" + map_dtToPrint[node.datatype_converted] 

            if isinstance(node, VarRefNode):
                if node.datatype_original == DT_ARRAY_INT \
                    or node.datatype_original == DT_ARRAY_FLOAT \
                    or node.datatype_original == DT_ARRAY_CHAR:

                    dimension = node.dimension_converted[1]                    
                    result += "[" + str(dimension) + "]"
            
            result += " " 

            if isinstance(node, CConNode):
                # For Ccon we have add single quote around the value
                result += "'" + str(node.value) + "'" + ")"
            else:
                result += str(node.value) + ")"

            return result
        elif isinstance(node, BinaryNode):
            bin_node = node
            result = "#($" + bin_node.node_type
            # Data Type Add
            result += ":" + map_dtToPrint[node.datatype_original] + ":" + map_dtToPrint[node.datatype_converted]

            if bin_node.getLeftChild() is not None:
                result += " " + bin_node.getLeftChild().accept(self)
            if bin_node.getRightChild() is not None:
                result += " " + bin_node.getRightChild().accept(self)
                
            result += ")"
            return result
        
        
        elif isinstance(node, UnaryNode):
            unary_node = node
            result = "#($"

            # Original Data Type
            result += unary_node.node_type + ":" + map_dtToPrint[unary_node.datatype_original]

            # If the datatype is an array (ident only)
            if isinstance(unary_node, IdentNode):
                if unary_node.datatype_original == DT_ARRAY_INT \
                    or unary_node.datatype_original == DT_ARRAY_FLOAT \
                    or unary_node.datatype_original == DT_ARRAY_CHAR:
                    result += "[" + str(unary_node.dimension_original[INDEX_DIM_ARA_IDENT_BOUND]) + "]"

            # Converted Data Type
            result += ":" + map_dtToPrint[node.datatype_converted]

            if isinstance(unary_node, IdentNode):
                if unary_node.datatype_converted == DT_ARRAY_INT \
                    or unary_node.datatype_converted == DT_ARRAY_FLOAT \
                    or unary_node.datatype_converted == DT_ARRAY_CHAR:
                    result += "[" + str(unary_node.dimension_converted[INDEX_DIM_ARA_IDENT_BOUND]) + "]"

            

            if hasattr(unary_node, "value"):
                # If the node has a value, we will add the value before going through the child
                # Example: #($arraydef  a  ...
                # Here the 'a' is the id of the $arraydef
                result += " " + unary_node.value

            # For $ident node, the second arguement could be None.
            # So, if it's not None, we recursively get the result for that too.
            if unary_node.only_child is not None:
                result += " " + unary_node.getOnlyChild().accept(self)
            
            result += ")"

            return result

        elif isinstance(node, MultiChildNode):
            multi_child_node = node
            result = "#($" + multi_child_node.node_type
            # Data Type Add
            result += ":" + map_dtToPrint[node.datatype_original] + ":" + map_dtToPrint[node.datatype_converted]

            children = multi_child_node.children
            for i in range(len(children)):
                if i == 0:
                    result += " "
                if isinstance(children[i], ASTNode):
                    result += children[i].accept(self)
                else:
                    result += children[i]
                if i != (len(children) - 1):
                    result += " "

            result += ")"

            return result

        elif isinstance(node, ExitNode):
            return "#($exit:"+  map_dtToPrint[node.datatype_original] + ":" + map_dtToPrint[node.datatype_converted] + ")"



 

class CompileVisitor(Visitor):
    def __init__(self):
        super().__init__()
        
        # Will be used to see if assembly failed
        self.success = True

        self.is_float_one_added = False

        # This will be used to create new labels for control flows
        self.label_counter = 0

        # Registers
        # A dictionary that keeps track of registers
        # Each item is a list: [Avaialable: bool, CurrentValue: int]
        self.reg_list = {
            "rdi": True,
            "rsi": True,
            "rcx": True,
            "rbx": True,
            "r8":  True,
            "r9":  True,
            "r10": True,
            "r11": True,
            "r12": True,
            "r13": True,
            "r14": True,
            "r15": True,
            "rdx": True,
            "rax": True,
            "rbp": True,
            "rsp": False,
        }

        self.float_reg_list = {
            'xmm0': True,
            'xmm1': True,
            'xmm2': True,
            'xmm3': True,
            'xmm4': True,
            'xmm5': True,
            'xmm6': True,
            'xmm7': True,
        }

        self.mapper_conditon_emit_code = {
            MAP_CND_CD_GT_INT : "jle", 
            MAP_CND_CD_GE_INT : "jl", 
            MAP_CND_CD_LT_INT : "jge", 
            MAP_CND_CD_LE_INT : "jg", 
            MAP_CND_CD_EQ_INT : "jne", 
            MAP_CND_CD_NE_INT : "je",
            MAP_CND_CD_GT_FLOAT: "jbe",
            MAP_CND_CD_GE_FLOAT: "jb",
            MAP_CND_CD_LT_FLOAT: "jae",
            MAP_CND_CD_LE_FLOAT: "ja",
            MAP_CND_CD_EQ_FLOAT: "jne",
            MAP_CND_CD_NE_FLOAT: "je" 


        }

        # Keeps track of the current offset
        self.current_offset = 8
        
        # A dictionary to keep track of the offsets of individual variables
        # Each item will be "IDENT_NAME" = [BASE_PTR: str, POSITIVE_INT_VALUE]
        # BASE_PTR could be the stack pointer or an ARP
        # self.var_offset = {}

        self.current_function = ""

        # self.var_offset_stack = {}
        self.symbol_table = {}

        # Starting of at -16, beacuse the call to main function
        # aligns -8, and we pushed rbp at the beginning on purpose
        # to align it to -16
        self.current_stack_alignment = 16
    


        # To keep track of str_constants (StrNode)
        # We will use this to generate unique values to add str constants to the data section area 
        self.str_cons_count = 0
        self.float_count = 0

        # All Assembly Codes

        # Data Section of assembly.
        self.asm_data_section = [
            '\t .section .rodata\n',
            '.char_wformat: .string "%c\\n"',
            '.int_wformat: .string "%d\\n"',
            '.float_wformat: .string "%f\\n"',
            '.str_wformat: .string "%s\\n"',
            '.char_rformat: .string "%c"',
            '.int_rformat: .string "%ld"',
            '.float_rformat: .string "%f"',
            ''
        ]


        # ASM for Function Directives
        self.asm_main =[
        ]
        
        self.asm_code = []

    def generateAssembly(self, filename):
        with open(filename, 'w') as file:
            file.write('\n'.join(self.asm_data_section))
            file.write('\n\n')
            file.write('\n'.join(self.asm_main))
            file.write('\n'.join(self.asm_code))

    # Aligns Stack at 16 bytes.
    # Returns True if stack was manipulated, False otherwise
    def alignStack(self, alignment=STACK_ALIGNMENT):
        if self.current_stack_alignment % alignment != 0:
            tmp = alignment - (self.current_stack_alignment % alignment)
            self.asm_code.append(f"\tsubq ${tmp}, %rsp")
            self.current_stack_alignment += tmp
            return True
        else:
            return False




    # Utility Functions
    # def getNextAvailableReg(self, type=REG_INT, set=REG_SET_ALL):
    def getNextAvailableReg(self, type=REG_INT):
        if type == REG_INT:
            for reg in self.reg_list:
                if self.reg_list[reg]:
                    self.reg_list[reg] = False
                    return reg
            raise("No Available Register")
        elif type == REG_FLOAT:
            for reg in self.float_reg_list:
                if self.float_reg_list[reg]:
                    self.float_reg_list[reg] = False
                    return reg
            raise("No Register Available ")


    
    def freeRegister(self, reg):
        if reg in self.reg_list:
            self.reg_list[reg] = True
        elif reg in self.float_reg_list:
            self.float_reg_list[reg] = True
        else:
            raise("Invalid Register")

    def isRegAvailable(self, reg):
        if reg in self.reg_list:
            return self.reg_list[reg]
        elif reg in self.float_reg_list:
            return self.float_reg_list[reg]
        else:
            raise("Invalid Register")

    def getDifferentSizeOfReg(self, reg, size):
        if reg not in self.reg_list:
            raise("Invalid Register")
        else:
            map_size_to_idx = {
                SIZE_QUAD_WORD: 0,
                SIZE_DBL_WORD: 1,
                SIZE_WORD: 2,
                SIZE_BYTE: 3
            }

            all_reg_list = {
                "rdi": ["rdi", "edi", "di", "dil"],
                "rsi": ["rsi", "esi", "si", "sil"],
                "rdx": ["rdx", "edx", "dx", "dl"],
                "rcx": ["rcx", "ecx", "cx", "cl"],
                "rax": ["rax", "eax", "ax", "al"],
                "rbx": ["rbx", "ebx", "bx", "bl"],
                "rbp": ["rbp", "ebp", "bp", "bpl"],
                "rsp": ["rsp", "esp", "sp", "spl"],
                "r8":  ["r8", "r8d", "r8w", "r8b"],
                "r9":  ["r9", "r9d", "r9w", "r9b"],
                "r10": ["r10", "r10d", "r10w", "r10b"],
                "r11": ["r11", "r11d", "r11w", "r11b"],
                "r12": ["r12", "r12d", "r12w", "r12b"],
                "r13": ["r13", "r13d", "r13w", "r13b"],
                "r14": ["r14", "r14d", "r14w", "r14b"],
                "r15": ["r15", "r15d", "r15w", "r15b"],
            }

            size_index = map_size_to_idx[size]

            return all_reg_list[reg][size_index]
        
    def storeRegValTemporarily(self, reg: str):
        if reg in self.reg_list:
            # Int Register
            tmp_reg = self.getNextAvailableReg(REG_INT)
            self.asm_code.append(f"\tmovq %{reg}, %{tmp_reg}")
            self.freeRegister(reg)
            return tmp_reg

    def freeRegisterTemporarily(self, needed_reg):
        if self.isRegAvailable(needed_reg):
            return INVALID_REG
        else:
            tmp_reg = self.storeRegValTemporarily(needed_reg)
            return tmp_reg

    def revertTemporaryRegister(self, tmp_reg, original_reg):
        if tmp_reg != INVALID_REG:
            self.asm_code.append(f"\tmovq %{tmp_reg}, %{original_reg}")

    def convertDataType(self, type, int_reg, float_reg):
        if type == FUNC_ARG_CVT_DT_I_TO_F:
            # Need to set XMM reg = 0 before the conversion
            self.asm_code.append(f'\tpxor %{float_reg}, %{float_reg}')
            # Conversion
            self.asm_code.append(f'\tcvtsi2ss %{int_reg}, %{float_reg}')
            # Free the int register
            self.freeRegister(int_reg)
        
        elif type == FUNC_ARG_CVT_DT_F_TO_I:
            # Convert
            self.asm_code.append(f'\tcvttss2si %{float_reg}, %{int_reg}')
            
            # Free the Float Reg
            self.freeRegister(float_reg)

    
    def addFloatOneToDataSection(self):
        if not self.is_float_one_added:
            self.asm_data_section.append(f'.float_one: .float 1.0')


    def visit(self, node):
        if node.datatype_original in ERRORS:
            self.success = False
            
        
        if(isinstance(node, ProgNode)):
            # Process Vlist
            # Instead of accepting the visitor, we will directly
            # add all the asm code here, because this vlist is a list of global variables
            # which is different than the other vlist.
            
            for vdecl_node in node.left_child.children:
                for ident_node in vdecl_node.right_child.children:
                    if ident_node.datatype_original == DT_ARRAY_INT or \
                        ident_node.datatype_original == DT_ARRAY_CHAR:
                        dim_idx_type = ident_node.dimension_original[INDEX_DIM_ARA_IDENT_TYPE]
                        dim_idx_bound = ident_node.dimension_original[INDEX_DIM_ARA_IDENT_BOUND]

                        if dim_idx_type == DT_INT:
                            self.asm_data_section.append(f'.comm {ident_node.value}, {dim_idx_bound*8}, 8')


                    else:
                        self.asm_data_section.append(f'.comm {ident_node.value}, 8, 8')
                    # self.var_offset[ident_node.value] = [None, GLOBAL_DATA]

            node.getRightChild().accept(self)

        if(isinstance(node, FlistNode)):
            # Prcess the fdecl nodes
            for fdecl_node in node.children:
                fdecl_node.accept(self)

        elif(isinstance(node, FDeclNode)):
            func_name = node.properties[IDX_FNODE_PROP_ID] 

            # Add the symbol table entry for the function
            self.current_offset = 8
            self.symbol_table[func_name] = dict()
            self.current_function = func_name


            # Adding the Assembly head section for the function
            self.asm_code.append(f'\t.text')
            self.asm_code.append(f'\t.globl {func_name}')
            self.asm_code.append(f'\t.type {func_name}, @function')
            self.asm_code.append(f'{func_name}:')
            self.asm_code.append(f'\tpushq %rbp')
            self.asm_code.append(f'\tmovq %rsp, %rbp')

            # Go through the parameter list here
            parameter_registers_int = ['r9', 'r8', 'rcx', 'rdx', 'rsi', 'rdi']
            parameter_registers_float = ['xmm5', 'xmm4', 'xmm3', 'xmm2', 'xmm1', 'xmm0']

            for pnode in node.properties[IDX_FNODE_PROP_PLIST].children:
                if pnode.right_child.datatype_converted == DT_INT or \
                 pnode.right_child.datatype_converted == DT_CHAR:
                    reg = parameter_registers_int.pop()
                    parameter_registers_float.pop()
                    self.asm_code.append(f'\tmovq %{reg}, -{self.current_offset}(%rbp)')
                elif pnode.right_child.datatype_converted == DT_FLOAT:
                    reg = parameter_registers_float.pop()
                    parameter_registers_int.pop()
                    self.asm_code.append(f'\tmovss %{reg}, -{self.current_offset}(%rbp)')

                self.symbol_table[func_name][pnode.right_child.value] = ["rbp", self.current_offset] 
                self.current_offset += 8



            # Go through the varlist here
            node.properties[IDX_FNODE_PROP_VLIST].accept(self)


            # Go thought the cmpd statement of the function
            node.properties[IDX_FNODE_PROP_STMTS].accept(self)

            # Epilog Area
            if func_name == "main":
                self.asm_code.append(f'\tleave')
                self.asm_code.append(f'\tret')
                self.asm_code.append(f'')
            else:
                self.asm_code.append(f'\tleave')
                self.asm_code.append(f'\tret')


        elif isinstance(node, FCallNode):

            # Precall

            # Save Registers in the stack
            pushed_registers = []
            for reg in self.reg_list:
                if self.reg_list[reg] == False:
                    if reg == "rbp" or reg == "rsp":
                        continue
                    # Register is in use, so save it in the stack
                    self.asm_code.append(f'\tpushq %{reg}')
                    pushed_registers.append(reg)
                    self.current_stack_alignment += 8

            # Set Parmeter values in the registers after evaluation
            # parameter_register in reverse order
            parameter_registers_int = ['r9', 'r8', 'rcx', 'rdx', 'rsi', 'rdi']
            # Parameter Registers for float in reverse order
            parameter_registers_float = ['xmm5', 'xmm4', 'xmm3', 'xmm2', 'xmm1', 'xmm0']
         
            # Pre call, go through the list of arguements
            arg_list = node.only_child
            arg_regs = []
            for arg_node in arg_list.children:
                ret_reg = arg_node.accept(self)
                arg_regs.append(ret_reg)
            
            for arg_reg in arg_regs:
                if arg_reg in self.reg_list:
                    parameter_register = parameter_registers_int.pop()
                    parameter_registers_float.pop()
                    self.asm_code.append(f'\tmovq %{arg_reg}, %{parameter_register}')
                elif arg_reg in self.float_reg_list:
                    parameter_register = parameter_registers_float.pop()
                    parameter_registers_int.pop()
                    self.asm_code.append(f'\tmovss %{arg_reg}, %{parameter_register}')

                self.freeRegister(arg_reg)


            # Align Stack before calling Function
            was_stack_manipulated = self.alignStack()
                    
            # Call the function
            self.asm_code.append(f'\tcall {node.value}')

            if node.datatype_original == DT_INT: 
                new_int_reg = self.getNextAvailableReg(REG_INT)
                self.asm_code.append(f'\tmovq %rax, %{new_int_reg}')
                ret_reg = new_int_reg
            elif node.datatype_original == DT_FLOAT:
                new_float_reg = self.getNextAvailableReg(REG_FLOAT)
                self.asm_code.append(f'\tmovss %xmm0, %{new_float_reg}')
                ret_reg = new_float_reg
            
            
            # Post call, free the registers
            # Restore the registers from the stack
            if was_stack_manipulated:
                self.asm_code.append(f'\taddq $8, %rsp')
            for reg in pushed_registers:
                self.asm_code.append(f'\tpopq %{reg}')

            try:
                self.freeRegister(res_reg)
            except:
                pass

            return ret_reg

        elif isinstance(node, PCallNode):
            # Precall

            # Save Registers in the stack
            pushed_registers = []
            for reg in self.reg_list:
                if self.reg_list[reg] == False:
                    if reg == "rbp" or reg == "rsp":
                        continue
                    # Register is in use, so save it in the stack
                    self.asm_code.append(f'\tpushq %{reg}')
                    pushed_registers.append(reg)
                    self.current_stack_alignment += 8

            # Set Parmeter values in the registers after evaluation
            # parameter_register in reverse order
            parameter_registers_int = ['r9', 'r8', 'rcx', 'rdx', 'rsi', 'rdi']
            # Parameter Registers for float in reverse order
            parameter_registers_float = ['xmm5', 'xmm4', 'xmm3', 'xmm2', 'xmm1', 'xmm0']
         
            # Pre call, go through the list of arguements
            arg_list = node.only_child
            arg_regs = []
            for arg_node in arg_list.children:
                ret_reg = arg_node.accept(self)
                arg_regs.append(ret_reg)
            
            for arg_reg in arg_regs:
                if arg_reg in self.reg_list:
                    parameter_register = parameter_registers_int.pop()
                    parameter_registers_float.pop()
                    self.asm_code.append(f'\tmovq %{arg_reg}, %{parameter_register}')
                elif arg_reg in self.float_reg_list:
                    parameter_register = parameter_registers_float.pop()
                    parameter_registers_int.pop()
                    self.asm_code.append(f'\tmovss %{arg_reg}, %{parameter_register}')

                self.freeRegister(arg_reg)


            # Align Stack before calling Function
            was_stack_manipulated = self.alignStack()
                    
            # Call the function
            self.asm_code.append(f'\tcall {node.value}')

            
            # Post call, free the registers
            # Restore the registers from the stack
            if was_stack_manipulated:
                self.asm_code.append(f'\taddq $8, %rsp')
            for reg in pushed_registers:
                self.asm_code.append(f'\tpopq %{reg}')





        elif isinstance(node, VarListNode):
            for vdecl_node in node.children:
                vdecl_node.accept(self)
        
        elif isinstance(node, VarDecNode):
            type = node.left_child.value

            # Var Count = Number of Ident in the Ilist.children
            var_count = len(node.right_child.children)
            array_len = -1

            # Assign space in the stack
            if type == "int":
                sub_from_stack = var_count*DT_SIZE_INT
                # self.asm_code.append(f'\tsub ${var_count*DT_SIZE_INT}, %rsp')
                # self.current_stack_alignment += (var_count*DT_SIZE_INT)
            
                # Storing the Offsets of each ident
                for ident_node in node.right_child.children:
                    if len(ident_node.dimension_converted) != 0:
                        # This is an array, so we have to allocate space accordingly 
                        if ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_TYPE] == DT_INT:
                            # THe index type is int, so we can allocate SIZE*index_value 
                            # Example: a[10] -> would allocate space for 10 integers.
                            # However, we need take 1 integer out, because it has already been
                            # added by the previous var_count*SIZE operation.
                            
                            array_len = (ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_BOUND])
                        elif ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_TYPE] == DT_CHAR:
                            # The index type is char
                            # So we have to find how many items from 'a' to curr index val

                            array_len =  ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_BOUND] - ord('a') + 1
                        sub_from_stack += (array_len-1) * DT_SIZE_INT
                        self.current_offset += (array_len-1)* DT_SIZE_INT
                        # self.var_offset[ident_node.value] = ["rbp", self.current_offset]
                        self.symbol_table[self.current_function][ident_node.value] = ["rbp", self.current_offset]
                    else:
                        # self.var_offset[ident_node.value] = ["rbp", self.current_offset]
                        self.symbol_table[self.current_function][ident_node.value] = ["rbp", self.current_offset]
                    
                    self.current_offset +=  DT_SIZE_INT

            elif type == "float":
                sub_from_stack = var_count*DT_SIZE_FLOAT
                # self.asm_code.append(f'\tsub ${var_count*DT_SIZE_FLOAT}, %rsp')
                # self.current_stack_alignment += (var_count*DT_SIZE_FLOAT)
            
                # Storing the Offsets of each ident
                for ident_node in node.right_child.children:
                    if len(ident_node.dimension_original) != 0:
                        # It's an array
                        if ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_TYPE] == DT_INT:
                            # THe index type is int, so we can allocate SIZE*index_value 
                            # Example: a[10] -> would allocate space for 10 integers.
                            # However, we need take 1 integer out, because it has already been
                            # added by the previous var_count*SIZE operation.
                            
                            array_len = (ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_BOUND])
                        if ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_TYPE] == DT_CHAR:
                            # The index type is char
                            # So we have to find how many items from 'a' to curr index val

                            array_len =  ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_BOUND] - ord('a') + 1
                        sub_from_stack += (array_len-1)*DT_SIZE_FLOAT
                        self.current_offset += (array_len-1)*DT_SIZE_FLOAT
                        # self.var_offset[ident_node.value] = ["rbp", self.current_offset]
                        self.symbol_table[self.current_function][ident_node.value] = ["rbp", self.current_offset]

                    else:
                        # self.var_offset[ident_node.value] = ["rbp", self.current_offset]
                        self.symbol_table[self.current_function][ident_node.value] = ["rbp", self.current_offset]

                    self.current_offset += DT_SIZE_FLOAT

            elif type == "char":
                sub_from_stack = var_count*DT_SIZE_CHAR

                # Storing the Offsets of each ident
                for ident_node in node.right_child.children:
                    if len(ident_node.dimension_converted) != 0:
                        # IT's an array
                        if ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_TYPE] == DT_INT:
                            # THe index type is int, so we can allocate SIZE*index_value 
                            # Example: a[10] -> would allocate space for 10 integers.
                            # However, we need take 1 integer out, because it has already been
                            # added by the previous var_count*SIZE operation.

                            array_len = (ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_BOUND])
                        elif ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_TYPE] == DT_CHAR:
                            # The index type is char
                            # So we have to find how many items from 'a' to curr index val
                            array_len =  ident_node.dimension_converted[INDEX_DIM_ARA_IDENT_BOUND] - ord('a') + 1

                        sub_from_stack += (array_len-1)*DT_SIZE_CHAR
                        self.current_offset += (array_len-1)*DT_SIZE_CHAR
                        # self.var_offset[ident_node.value] = ["rbp", self.current_offset]
                        
                        self.symbol_table[self.current_function][ident_node.value] = ["rbp", self.current_offset]
                    else:
                        # self.var_offset[ident_node.value] = ["rbp", self.current_offset]
                        self.symbol_table[self.current_function][ident_node.value] = ["rbp", self.current_offset]

                    self.current_offset += DT_SIZE_CHAR

            self.asm_code.append(f'\tsub ${sub_from_stack}, %rsp')
            self.current_stack_alignment += sub_from_stack

            # Align the Stack here, so that it doesn't cause problems with the control flow
            if self.current_stack_alignment%16 != 0:
                tmp = 16 - (self.current_stack_alignment%16)
                self.asm_code.append(f'\tsub ${tmp}, %rsp')
                self.current_stack_alignment += tmp

            

        elif isinstance(node, VarRefNode):
            var_ident = node.value
            is_global = False
            try:
                base_reg, var_offset = self.symbol_table[self.current_function][var_ident]
            except:
                # It's a global variable
                is_global = True
                 
            if is_global:
                # We can call it directly by name as it's a global data
                if node.datatype_original == DT_INT:
                    new_reg_int = self.getNextAvailableReg(REG_INT)
                    self.asm_code.append(f'\tmovq {var_ident}(%rip), %{new_reg_int}')

                    if node.datatype_converted == DT_FLOAT:
                        new_reg_float = self.getNextAvailableReg(REG_FLOAT)
                        self.convertDataType(FUNC_ARG_CVT_DT_I_TO_F, new_reg_int, new_reg_float)
                        return new_reg_float
                    return new_reg_int
                
                elif node.datatype_original == DT_FLOAT:
                    new_reg_float = self.getNextAvailableReg(REG_FLOAT)
                    self.asm_code.append(f'\tmovss {var_ident}(%rip), %{new_reg_float}')

                    if node.datatype_converted == DT_INT:
                        new_reg_int = self.getNextAvailableReg(REG_INT)
                        self.convertDataType(FUNC_ARG_CVT_DT_F_TO_I, new_reg_int, new_reg_float)
                        return new_reg_int
                    return new_reg_float

                elif node.datatype_original == DT_CHAR: 
                    new_reg_int = self.getNextAvailableReg(REG_INT)
                    self.asm_code.append(f'\tmovq {var_ident}(%rip), %{new_reg_int}')
                    return new_reg_int
            else:
                # Not Global Data. Get Value from Stack.
                if node.datatype_original == DT_INT:
                    new_reg_int = self.getNextAvailableReg(REG_INT)
                    self.asm_code.append(f'\tmovq -{var_offset}(%{base_reg}), %{new_reg_int}')

                    if node.datatype_converted == DT_FLOAT or \
                        node.datatype_converted == DT_ARRAY_FLOAT:
                        new_reg_float = self.getNextAvailableReg(REG_FLOAT)
                        self.convertDataType(FUNC_ARG_CVT_DT_I_TO_F, new_reg_int, new_reg_float)
                        return new_reg_float
                    return new_reg_int
                
                elif node.datatype_original == DT_FLOAT:
                    new_reg_float = self.getNextAvailableReg(REG_FLOAT)
                    # self.asm_code.append(f'\tmovss -{var_offset+DT_DBL_PR_FLOAT_DIFF}(%{base_reg}), %{new_reg_float}')
                    self.asm_code.append(f'\tmovss -{var_offset}(%{base_reg}), %{new_reg_float}')

                    if node.datatype_converted == DT_INT or \
                        node.datatype_converted == DT_ARRAY_INT:
                        new_reg_int = self.getNextAvailableReg(REG_INT)
                        self.convertDataType(FUNC_ARG_CVT_DT_F_TO_I, new_reg_int, new_reg_float)
                        return new_reg_int
                    return new_reg_float

                elif node.datatype_original == DT_CHAR:
                    new_reg_int = self.getNextAvailableReg(REG_INT)
                    self.asm_code.append(f'\tmovq -{var_offset}(%{base_reg}), %{new_reg_int}')

                    return new_reg_int


        elif isinstance(node, ArrayRefNode):
            var_ident = node.value
            is_global = False

            # Go Through the index expression
            reg_ind = node.only_child.accept(self) 
            if node.only_child.datatype_original == DT_CHAR:
                # The index is char, we have to convert it to int
                self.asm_code.append(f'\tsubq $97, %{reg_ind}')

            # base_reg, var_offset = self.var_offset[var_ident]
            try:
                base_reg, var_offset = self.symbol_table[self.current_function][var_ident]
            except:
                # It's a global variable
                is_global = True
            if is_global:
                new_reg_int = self.getNextAvailableReg(REG_INT)
                self.asm_code.append(f'\tleaq (, %{reg_ind},{DT_SIZE_INT}), %{new_reg_int}')
                self.asm_code.append(f'\tleaq {var_ident}(%rip), %{reg_ind}')
                self.asm_code.append(f'\tmovq (%{new_reg_int},%{reg_ind}), %{reg_ind}')
                self.freeRegister(new_reg_int)
                return reg_ind
            
            if node.datatype_original == DT_ARRAY_INT:
                new_reg_int = self.getNextAvailableReg(REG_INT)

                if is_global:
                    self.asm_code.append(f'\tmovq {var_ident}(%rip,%{reg_ind},{DT_SIZE_INT}), %{new_reg_int}')
                else:
                    self.asm_code.append(f'\tmovq -{var_offset}(%{base_reg},%{reg_ind},{DT_SIZE_INT}), %{new_reg_int}')
                new_reg = new_reg_int
                if node.datatype_converted == DT_FLOAT or node.datatype_converted == DT_ARRAY_FLOAT:
                    new_reg_float = self.getNextAvailableReg(REG_FLOAT)
                    self.convertDataType(FUNC_ARG_CVT_DT_I_TO_F, new_reg_int, new_reg_float)
                    new_reg = new_reg_float
                
            if node.datatype_original == DT_ARRAY_FLOAT:
                new_reg_float = self.getNextAvailableReg(REG_FLOAT)
                
                if is_global:
                    self.asm_code.append(f'\tmovss {var_ident}(%rip,%{reg_ind},{DT_SIZE_FLOAT}), %{new_reg_float}')
                else:
                    self.asm_code.append(f'\tmovss -{var_offset}(%{base_reg},%{reg_ind},{DT_SIZE_FLOAT}), %{new_reg_float}')
                
                new_reg = new_reg_float
                # if (node.datatype_original != node.datatype_converted) and \
                #    (node.datatype_original == DT_INT or node.datatype_original == DT_ARRAY_INT):
                if node.datatype_converted == DT_INT or node.datatype_converted == DT_ARRAY_INT:
                    new_reg_int = self.getNextAvailableReg(REG_INT)
                    self.convertDataType(FUNC_ARG_CVT_DT_F_TO_I, new_reg_int, new_reg_float)
                    new_reg = new_reg_int

            
            if node.datatype_original == DT_ARRAY_CHAR:
                new_reg_int = self.getNextAvailableReg(REG_INT)

                if is_global:
                    self.asm_code.append(f'\tmovq {var_ident}(%rip,%{reg_ind},{DT_SIZE_CHAR}), %{new_reg_int}')
                else:
                    self.asm_code.append(f'\tmovq -{var_offset}(%{base_reg},%{reg_ind},{DT_SIZE_INT}), %{new_reg_int}')
                
                new_reg = new_reg_int

            self.freeRegister(reg_ind)
            return new_reg

        elif isinstance(node, ArrayDefNode):
            var_ident = node.value
            reg_ind = node.only_child.accept(self)

            is_global = False
            try:
                base_reg, var_offset = self.symbol_table[self.current_function][var_ident]
            except:
                is_global = True

            if is_global:
                new_int_reg = self.getNextAvailableReg(REG_INT)
                self.asm_code.append(f'\tleaq (,%{reg_ind},{DT_SIZE_INT}), %{new_int_reg}')
                self.asm_code.append(f'\tleaq {var_ident}(%rip), %{reg_ind}')
                self.asm_code.append(f'\taddq %{new_int_reg}, %{reg_ind}')
                self.freeRegister(new_int_reg)
                res_reg = reg_ind
            else:
                new_int_reg = self.getNextAvailableReg(REG_INT)
                if node.datatype_original == DT_ARRAY_INT or\
                   node.datatype_original == DT_ARRAY_CHAR:
                    self.asm_code.append(f'\tleaq -{var_offset}(%{base_reg}), %{new_int_reg}')
                    res_reg = new_int_reg
                elif node.datatype_original == DT_ARRAY_FLOAT:
                    new_float_reg = self.getNextAvailableReg(REG_FLOAT)
                    self.asm_code.append(f'\tleaq -{var_offset}(%{base_reg}), %{new_float_reg}') 
                    res_reg = new_float_reg
            
            return res_reg



        elif isinstance(node, CmpdNode):
            for stmt_node in node.children:
                reg = stmt_node.accept(self)
                try:
                    self.freeRegister(reg)
                except:
                    pass

        elif isinstance(node, ReadNode):
            is_global = False
            if node.only_child.datatype_converted == DT_INT or\
                node.only_child.datatype_converted == DT_CHAR or \
                node.only_child.datatype_converted == DT_ARRAY_INT or \
                node.only_child.datatype_converted == DT_ARRAY_CHAR:
                format = "int"
            elif node.only_child.datatype_converted == DT_FLOAT:
                format = "float"

            if isinstance(node.only_child, ArrayDefNode):
                res_reg = node.only_child.accept(self)
                tmp_reg = INVALID_REG 

                if not self.isRegAvailable("rsi"):
                    tmp_reg = self.freeRegisterTemporarily("rsi")

                self.asm_code.append(f'movq %{res_reg}, %rsi') 

                self.asm_code.append(f'\tleaq .{format}_rformat(%rip), %rdi')
                self.asm_code.append(f'\tmovq $0, %rax')

                # Stack Alignment
                            
                # if self.current_stack_alignment%16 != 0:
                    # tmp = 16 - (self.current_stack_alignment%16)
                
                    # # Aliging stack pointer to 16-byte
                    # self.asm_code.append(f'\tsub ${tmp}, %rsp')

                    # self.current_stack_alignment += tmp

                was_stack_manipulated = self.alignStack()

                self.asm_code.append(f'\tcall scanf')

                if was_stack_manipulated:
                    self.asm_code.append(f'\taddq $8, %rsp')
                    self.current_stack_alignment -= 8
            
                if tmp_reg != INVALID_REG:
                    self.revertTemporaryRegister(tmp_reg, "rsi")

            else:
                var_ident = node.only_child.value
                # Get the offset in the stack
                # base_reg, var_offset = self.var_offset[var_ident]
                try:
                    base_reg, var_offset = self.symbol_table[self.current_function][var_ident]
                except:
                    is_global = True


                tmp_reg = INVALID_REG 
                if is_global:
                    if not self.isRegAvailable("rsi"):
                        tmp_reg = self.freeRegisterTemporarily("rsi") 


                    if isinstance(node.only_child, ArrayDefNode):
                        # Go through the index expression
                        reg_ind = node.only_child.only_child.accept(self) 


                    self.asm_code.append(f'\tleaq {var_ident}(%rip), %rsi')

                else:
                    if self.isRegAvailable("rsi"):
                        if node.only_child.datatype_converted == DT_INT:
                            self.asm_code.append(f'\tleaq -{var_offset}(%{base_reg}), %rsi')
                        elif node.only_child.datatype_converted == DT_FLOAT:
                            self.asm_code.append(f'\tleaq -{var_offset+SIZE_DBL_WORD}(%{base_reg}), %rsi')
                    else:
                        tmp_reg = self.freeRegisterTemporarily("rsi")
                        if node.only_child.datatype_converted == DT_INT:
                            self.asm_code.append(f'\tleaq -{var_offset}(%{base_reg}), %rsi')
                        elif node.only_child.datatype_converted == DT_FLOAT:
                            self.asm_code.append(f'\tleaq -{var_offset}(%{base_reg}), %rsi')

                self.asm_code.append(f'\tleaq .{format}_rformat(%rip), %rdi')
                self.asm_code.append(f'\tmovq $0, %rax')

                # Stack Alignment
                            
                # if self.current_stack_alignment%16 != 0:
                    # tmp = 16 - (self.current_stack_alignment%16)
                
                    # # Aliging stack pointer to 16-byte
                    # self.asm_code.append(f'\tsub ${tmp}, %rsp')

                    # self.current_stack_alignment += tmp

                was_stack_manipulated = self.alignStack()

                self.asm_code.append(f'\tcall scanf')

                if was_stack_manipulated:
                    self.asm_code.append(f'\taddq $8, %rsp')
                    self.current_stack_alignment -= 8
            
                if tmp_reg != INVALID_REG:
                    self.revertTemporaryRegister(tmp_reg, "rsi")

        elif(isinstance(node, WriteNode)):
            was_stack_manipulated = False
            val_reg = node.only_child.accept(self)
            isXmmMoved = False

            if node.only_child.datatype_converted ==  DT_STR:
                self.asm_code.append(
                    f'\tleaq .string_const{node.only_child.str_cons_count}(%rip), %rdi'
                )
                self.asm_code.append(
                    f'\tmov $0, %rax'
                )

                # Stack Alignment
                if self.current_stack_alignment%16 != 0:
                    tmp = 16 - (self.current_stack_alignment%16)
                    
                    # Aliging stack pointer to 16-byte
                    self.asm_code.append(f'\tsub ${tmp}, %rsp')
                    self.current_stack_alignment += tmp
                    was_stack_manipulated = True

                self.asm_code.append(f'\tcall printf')
                if was_stack_manipulated:
                    self.asm_code.append(f'\tadd ${tmp}, %rsp')
                    self.current_stack_alignment -= tmp
                    was_stack_manipulated = False

                return
                
            elif node.only_child.datatype_converted ==  DT_INT \
                or node.only_child.datatype_converted == DT_ARRAY_INT:
                self.asm_code.append(f'\tmovq %{val_reg}, %rsi')
                self.asm_code.append(f'\tleaq .int_wformat(%rip), %rdi')
                self.asm_code.append(f'\tmov $0, %rax')
            
            elif node.only_child.datatype_converted == DT_FLOAT or \
                node.only_child.datatype_converted == DT_ARRAY_FLOAT:
                # we need to store the value in xmm0 to print
                if val_reg == "xmm0":
                    self.asm_code.append(f'\tcvtss2sd %{val_reg}, %{val_reg}')
                else:
                    if not self.isRegAvailable("xmm0"):
                        # There is a valid data in xmm0, 
                        # so we need store it somewhere else
                        move_xmm_reg = self.getNextAvailableReg(REG_FLOAT)
                        self.asm_code.append(f"movss %xmm0, %{move_xmm_reg}")
                        isXmmMoved = True

                    self.asm_code.append(f'\tmovss %{val_reg}, %xmm0')
                    self.asm_code.append(f'\tcvtss2sd %xmm0, %xmm0')

                self.asm_code.append(f'\tleaq .float_wformat(%rip), %rdi')
                self.asm_code.append(f'\tmovq $1, %rax')

            elif node.only_child.datatype_converted == DT_CHAR or \
                node.only_child.datatype_converted == DT_ARRAY_CHAR:
                tmp_reg = self.freeRegisterTemporarily("rax")

                self.asm_code.append(f'\tmovq %{val_reg}, %rax')
                self.asm_code.append(f'\tmovsbq %al, %rax')
                self.asm_code.append(f'\tmovq %rax, %rdi')
                
                self.revertTemporaryRegister(tmp_reg, "rax")

            # Free val_reg
            try:
                self.freeRegister(val_reg)
            except:
                pass

            # Stack Alignment
            if self.current_stack_alignment%16 != 0:
                tmp = 16 - (self.current_stack_alignment%16)
                
                # Aliging stack pointer to 16-byte
                self.asm_code.append(f'\tsub ${tmp}, %rsp')
                self.current_stack_alignment += tmp
                was_stack_manupulated = True
                                
            
            call_func_names = {
                DT_INT: 'printf',
                DT_FLOAT: 'printf',
                DT_CHAR: 'putchar',
                DT_ARRAY_INT: 'printf',
                DT_ARRAY_FLOAT: 'printf',
                DT_ARRAY_CHAR: 'putchar'
            }
            call_func = call_func_names[node.only_child.datatype_converted]
            self.asm_code.append(f'\tcall {call_func}')

            if call_func == 'putchar':
                # we have to add a new line add the end for putchar as it doesn't do that automatically
                self.asm_code.append(f'\tmovq $10, %rax')
                self.asm_code.append(f'\tmovsbq %al, %rax')
                self.asm_code.append(f'\tmovq %rax, %rdi')
                self.asm_code.append(f'\tcall putchar')

            if was_stack_manipulated == True:
                self.asm_code.append(f'\taddq $8, %rsp')
                self.current_stack_alignment -= 8
                was_stack_manipulated = False

            if isXmmMoved:
                # Restoring the value of xmm0
                self.asm_code.append(f'movss %{move_xmm_reg}, %xmm0')
                self.freeRegister(move_xmm_reg)

        elif isinstance(node, AssignNode):
            var_ident = node.left_child.value
            is_global = False

            # Get the offset in the stack
            # base_reg, var_offset = self.var_offset[var_ident]
            try:
                base_reg, var_offset = self.symbol_table[self.current_function][var_ident]
            except:
                is_global = True

            right_op_reg = node.right_child.accept(self)

            # if is_global:
                # self.asm_code.append(f'\tmovq %{right_op_reg}, {var_ident}(%rip)')

            # else:

            # For arrays we need to check the left child original type
            # Regular types can be checked from right child converted type
            if node.left_child.datatype_original == DT_ARRAY_INT or\
                node.left_child.datatype_original == DT_ARRAY_CHAR:
                # We need to go inside index for the offset
                reg_ind = node.left_child.only_child.accept(self)

                if node.left_child.only_child.datatype_original == DT_CHAR:
                    # Index is a char. So convert it to integer by subbing 97
                    self.asm_code.append(f'\tsub $97, %{reg_ind}')


                if is_global:
                    self.asm_code.append(f'\tmovq %{right_op_reg}, {var_ident}(%rip,%{reg_ind},{DT_SIZE_INT})')
                else:
                    self.asm_code.append(f'\tmovq %{right_op_reg}, -{var_offset}(%{base_reg},%{reg_ind},{DT_SIZE_INT})')
                self.freeRegister(reg_ind)
            elif node.left_child.datatype_original == DT_ARRAY_FLOAT:
                # Visit the index node
                reg_ind = node.left_child.only_child.accept(self)
                # Asm
                if is_global:
                    self.asm_code.append(f'\tmovss %{right_op_reg}, {var_ident}(%rip,%{reg_ind},{DT_SIZE_FLOAT})')
                else:
                    self.asm_code.append(f'\tmovss %{right_op_reg}, -{var_offset}(%{base_reg},%{reg_ind},{DT_SIZE_FLOAT})')
                self.freeRegister(reg_ind)

            elif node.right_child.datatype_original == DT_FLOAT:
                operation = 'movss'
                if node.left_child.datatype_converted == DT_INT:
                    # We need to convert the value to int
                    new_reg_int = self.getNextAvailableReg(REG_INT)
                    self.convertDataType(FUNC_ARG_CVT_DT_F_TO_I, new_reg_int, right_op_reg)
                    right_op_reg = new_reg_int
                    operation = 'movq'

                if is_global:
                    self.asm_code.append(f'\t{operation} %{right_op_reg}, {var_ident}(%rip)')
                else:
                    self.asm_code.append(f'\t{operation} %{right_op_reg}, -{var_offset}(%{base_reg})')

            elif node.right_child.datatype_converted == DT_INT:
                if is_global:
                    self.asm_code.append(f'\tmovq %{right_op_reg}, {var_ident}(%rip)')
                else:
                    self.asm_code.append(f'\tmovq %{right_op_reg}, -{var_offset}(%{base_reg})')

            elif node.right_child.datatype_converted == DT_FLOAT:
                if is_global:
                    self.asm_code.append(f'\tmovss %{right_op_reg}, {var_ident}(%rip)')
                else:
                    self.asm_code.append(f'\tmovss %{right_op_reg}, -{var_offset}(%{base_reg})')

            elif node.right_child.datatype_converted == DT_CHAR:
                # right_op_reg_byte = self.getDifferentSizeOfReg(right_op_reg, SIZE_BYTE)
                if is_global:
                    self.asm_code.append(f'\tmovb %{right_op_reg}, {var_ident}(%rip)')
                else:
                    self.asm_code.append(f'\tmovq %{right_op_reg}, -{var_offset}(%{base_reg})')


    
            self.freeRegister(right_op_reg)


        elif isinstance(node, (AddNode, SubNode)):
            left_op_reg = node.left_child.accept(self)
            right_op_reg = node.right_child.accept(self)

            if isinstance(node, AddNode):
                op = 'add'
                op_dbl = 'addl'
            elif isinstance(node, SubNode):
                op = 'sub'
                op_dbl = 'subl'
                # Switing the operands, bacause the x86 instruction is reversed for sub
                left_op_reg, right_op_reg = right_op_reg, left_op_reg

            if node.left_child.datatype_converted == DT_INT:
                self.asm_code.append(f'\t{op}q %{left_op_reg}, %{right_op_reg}')

            elif node.left_child.datatype_converted == DT_FLOAT:
                self.asm_code.append(f'\t{op}ss %{left_op_reg}, %{right_op_reg}')

            elif node.left_child.datatype_original == DT_CHAR:
                left_op_reg_dbl = self.getDifferentSizeOfReg(left_op_reg, SIZE_DBL_WORD)
                right_op_reg_dbl = self.getDifferentSizeOfReg(right_op_reg, SIZE_DBL_WORD)

                # These registers are holding leaq address, so, we can't add them.
                # We need to convert them to normal values
                self.asm_code.append(f'\tmovzbl (%{left_op_reg}), %{left_op_reg_dbl}')
                self.asm_code.append(f'\tmovzbl (%{right_op_reg}), %{right_op_reg_dbl}')
                self.asm_code.append(f'\t{op_dbl} %{left_op_reg_dbl}, %{right_op_reg_dbl}')
            
            self.freeRegister(left_op_reg)
            
            # Checking whethere we need to convert the data
            if node.datatype_original != node.datatype_converted:
                if node.datatype_converted == DT_INT:
                    # Need to convert to INT
                    new_reg_int = self.getNextAvailableReg(REG_INT)
                    self.convertDataType(FUNC_ARG_CVT_DT_F_TO_I, new_reg_int, right_op_reg)
                    return new_reg_int
                elif node.datatype_converted == DT_FLOAT:
                    # Need to convert to Float
                    new_reg_float = self.getNextAvailableReg(REG_FLOAT)
                    self.convertDataType(FUNC_ARG_CVT_DT_I_TO_F, right_op_reg, new_reg_float)
                    return new_reg_float
            return right_op_reg

        elif isinstance(node, (MulNode, DivNode)):
            if isinstance(node, MulNode):
                operation = "imulq"
                operation_float = "mulss"
            if isinstance(node, DivNode):
                operation = "idivq"
                operation_float = "divss"

            left_op_reg = node.left_child.accept(self)
            right_op_reg = node.right_child.accept(self)

            if node.left_child.datatype_converted == DT_INT:
                isRaxPushed = False
                isRdxPushed = False
                
                if left_op_reg != 'rax':
                    if not self.isRegAvailable("rax"):
                        # Storing the Rax Value in the stack
                        self.asm_code.append(f'\tpushq %rax')
                        isRaxPushed = True
                        self.current_stack_alignment += SIZE_QUAD_WORD
                    
                    self.asm_code.append(f'\tmovq %{left_op_reg}, %rax')
                
                if not self.isRegAvailable("rdx"):
                    self.asm_code.append(f'\tpushq %rdx')
                    isRdxPushed = True
                    self.current_stack_alignment += SIZE_QUAD_WORD
                
                # Sign exted rax to rdx
                self.asm_code.append(f'\tcltd')
                self.asm_code.append(f'\t{operation} %{right_op_reg}')

                # Moving my result back to a new reg
                res_reg = self.getNextAvailableReg()
                self.asm_code.append(f'\tmovq %rax, %{res_reg}')

                # Restoring Rdx, and Rax if they were pushed
                if isRdxPushed:
                    self.asm_code.append(f'\tpopq %rdx')
                    self.current_stack_alignment -= SIZE_QUAD_WORD
                if isRaxPushed:
                    self.asm_code.append(f'\tpopq %rax')
                    self.current_stack_alignment -= SIZE_QUAD_WORD

                self.freeRegister(right_op_reg)
                self.freeRegister(left_op_reg)
                return res_reg
            
            elif node.left_child.datatype_converted == DT_FLOAT:
                self.asm_code.append(f'\t{operation_float} %{right_op_reg}, %{left_op_reg}')
                self.freeRegister(right_op_reg)
                return left_op_reg

        elif isinstance(node, (AndNode, OrNode)):
            left_op_reg = node.left_child.accept(self)
            right_op_reg = node.right_child.accept(self)

            # If loper or roper is a float, we need to convert them to int
            if left_op_reg in self.float_reg_list:
                new_reg_int = self.getNextAvailableReg(REG_INT)
                self.convertDataType(FUNC_ARG_CVT_DT_F_TO_I, new_reg_int, left_op_reg)
                left_op_reg = new_reg_int

            if right_op_reg in self.float_reg_list:
                new_reg_int = self.getNextAvailableReg(REG_INT)
                self.convertDataType(FUNC_ARG_CVT_DT_F_TO_I, new_reg_int, right_op_reg)
                right_op_reg = new_reg_int
            
            # Res will hold the answer, tmp will be used for the cmov instructions
            res_reg = self.getNextAvailableReg(REG_INT)
            tmp_reg = self.getNextAvailableReg(REG_INT)
            
            if left_op_reg in self.reg_list:
                # This portion will do a int comparison to calculate the result of the and/or 
                if isinstance(node, AndNode):
                    self.asm_code.append(f'\tmovq $1, %{res_reg}')
                    self.asm_code.append(f'\tmovq $0, %{tmp_reg}')
                    self.asm_code.append(f'\tcmpq $0, %{left_op_reg}')
                    self.asm_code.append(f'\tcmove %{tmp_reg}, %{res_reg}')
                    self.asm_code.append(f'\tcmpq $0, %{right_op_reg}')
                    self.asm_code.append(f'\tcmove %{tmp_reg}, %{res_reg}')

                elif isinstance(node, OrNode):
                    self.asm_code.append(f'\tmovq $0, %{res_reg}')
                    self.asm_code.append(f'\tmovq $1, %{tmp_reg}')
                    self.asm_code.append(f'\tcmpq $0, %{left_op_reg}')
                    self.asm_code.append(f'\tcmovne %{tmp_reg}, %{res_reg}')
                    self.asm_code.append(f'\tcmpq $0, %{right_op_reg}')
                    self.asm_code.append(f'\tcmovne %{tmp_reg}, %{res_reg}')

            self.freeRegister(left_op_reg)
            self.freeRegister(right_op_reg)
            self.freeRegister(tmp_reg)
            return res_reg

        elif isinstance(node, NotNode):
            op_reg = node.only_child.accept(self)
            self.asm_code.append(f'\tnot %{op_reg}')
            return op_reg

        elif isinstance(node, IfNode):
            # Get Three labels
            label_else = f".L{self.label_counter}"
            label_next = f".L{self.label_counter+1}"
            self.label_counter += 2



            cnd_res_reg = node.children[IDX_IF_NODE_COND].accept(self)
            self.asm_code.append(f"\tcmp $1, %{cnd_res_reg}")

            if len(node.children) == 3:
                self.asm_code.append(f"\tjne {label_else}")
            else:
                self.asm_code.append(f'\tjne {label_next}')

            self.freeRegister(cnd_res_reg)

            # Process the then Statement,
            # It's a Cmpd Statement so it doesnt return a reg
            node.children[IDX_IF_NODE_THEN].accept(self)
            # jmp to next label
            self.asm_code.append(f"\tjmp {label_next}")

            if len(node.children) == 3:
                # Add the label
                # And process the ELSE statemnets now, and jmp to the next label
                self.asm_code.append(f"{label_else}:")
                node.children[IDX_IF_NODE_ELSE].accept(self)
                self.asm_code.append(f"\tjmp {label_next}")

            # Add the next label
            self.asm_code.append(f"{label_next}:")


            
        elif isinstance(node, WhileNode):
            label_while = f".L{self.label_counter}"
            label_next = f".L{self.label_counter+1}"
            self.label_counter+=2

            # add the while label before checking the codition
            self.asm_code.append(f"{label_while}:")
            # Process the codition
            cnd_res_reg = node.left_child.accept(self)
            
            # If condition fails, jump to the next label
            self.asm_code.append(f"\tcmp $1, %{cnd_res_reg}")
            self.asm_code.append(f"\tjne {label_next}")
            self.freeRegister(cnd_res_reg)

            # Else process the statements, and jump back to the while label
            node.right_child.accept(self)
            self.asm_code.append(f"\tjmp {label_while}")

            # Add the next Label
            self.asm_code.append(f"{label_next}:")



        elif isinstance(node, (GeNode, GtNode, LtNode, LeNode, EqNode, NeNode)):
            if isinstance(node, GtNode):
                opeartion = 'cmovg'
                operation_float = "seta"
            elif isinstance(node, GeNode):
                opeartion = 'cmovge'
                operation_float = "setae"
            elif isinstance(node, LtNode):
                opeartion = 'cmovl'
                operation_float = "setb"
            elif isinstance(node, LeNode):
                opeartion = 'cmovle'
                operation_float = "setbe"
            elif isinstance(node, EqNode):
                opeartion = 'cmove'
                operation_float = "sete"
            elif isinstance(node, NeNode):
                opeartion = 'cmovne'
                operation_float = "setne"

            left_op_reg = node.left_child.accept(self)
            right_op_reg = node.right_child.accept(self)

            if node.left_child.datatype_converted == DT_INT or node.left_child.datatype_converted == DT_ARRAY_INT or\
                node.left_child.datatype_converted == DT_CHAR or node.left_child.datatype_converted == DT_ARRAY_CHAR:    
                self.asm_code.append(f'\tcmp %{right_op_reg}, %{left_op_reg}')
                self.asm_code.append(f'\tmov $0, %{left_op_reg}')
                self.asm_code.append(f'\tmov $1, %{right_op_reg}')
                self.asm_code.append(f'\t{opeartion} %{right_op_reg}, %{left_op_reg}')
                
                self.freeRegister(right_op_reg)
                return left_op_reg

            elif node.left_child.datatype_converted == DT_FLOAT or node.left_child.datatype_converted == DT_ARRAY_FLOAT:
                cmp_res_reg = self.getNextAvailableReg()
                cmp_res_reg_dbl = self.getDifferentSizeOfReg(cmp_res_reg, SIZE_DBL_WORD)
                cmp_res_reg_byte = self.getDifferentSizeOfReg(cmp_res_reg, SIZE_BYTE)

                # Setting 0
                self.asm_code.append(f'\txor %{cmp_res_reg}, %{cmp_res_reg}')
                self.asm_code.append(f'\tcomiss %{right_op_reg}, %{left_op_reg}')
                # Setting cmp_res_reg based on the compare
                self.asm_code.append(f'\t{operation_float} %{cmp_res_reg_byte}')
                self.asm_code.append(f'\tmovzbq %{cmp_res_reg_byte}, %{cmp_res_reg}')


                self.freeRegister(left_op_reg)
                self.freeRegister(right_op_reg)
                return cmp_res_reg
        elif isinstance(node, IConNode):
            next_reg = self.getNextAvailableReg()
            self.asm_code.append(f'\tmovq ${node.value}, %{next_reg}')

            if node.datatype_converted == DT_FLOAT or \
            node.datatype_converted == DT_ARRAY_FLOAT:
                # We need to convert the value to a float.
                # So we need a XMM register
                new_reg_float = self.getNextAvailableReg(REG_FLOAT)
                
                self.convertDataType(type=FUNC_ARG_CVT_DT_I_TO_F, int_reg=next_reg, float_reg=new_reg_float)
                return new_reg_float
            return next_reg


        elif isinstance(node, FConNode):
            new_reg_float = self.getNextAvailableReg(REG_FLOAT)

            # Adding the float value to the static data section
            self.asm_data_section.append(f'.float{self.float_count}:\t.float {node.value}')

            # Storing the value in stack
            self.asm_code.append(f'\tmovss .float{self.float_count}(%rip), %{new_reg_float}')
            self.float_count+=1

            if node.datatype_converted == DT_INT or \
            node.datatype_converted == DT_ARRAY_INT:
                # Need to convert to Int
                new_reg_int = self.getNextAvailableReg(REG_INT)
                
                self.convertDataType(FUNC_ARG_CVT_DT_F_TO_I, new_reg_int, new_reg_float)
                return new_reg_int
            return new_reg_float
        

        elif isinstance(node, CConNode):
            next_reg = self.getNextAvailableReg()
            # next_reg_byte = self.getDifferentSizeOfReg(next_reg, SIZE_BYTE)
            char_ascii = ord(node.value.strip("'"))
            self.asm_code.append(f'\tmovq ${char_ascii}, %{next_reg}')
            return next_reg


        elif isinstance(node, StrNode):
            # Add the str_cons_count in the AST Node
            node.str_cons_count = self.str_cons_count
            self.str_cons_count += 1

            # Add the String to the data section
            self.asm_data_section.append(
                f'.string_const{node.str_cons_count}: .string "{node.value}\n"'
            )

        elif isinstance(node, RetNode):
            res_reg = node.only_child.accept(self)
            if res_reg in self.reg_list:
                self.asm_code.append(f'\tmovq %{res_reg}, %rax')
            elif res_reg in self.float_reg_list:
                self.asm_code.append(f'\tmovss %{res_reg}, %xmm0')
            else:
                raise Exception("Invalid Register")

            self.freeRegister(res_reg)



