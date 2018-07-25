from opencmiss import CMISS

#Initialising Coordinate System
coordinateSystem = CMISS.CoordinateSystem()
#Creates a wrapper that points to internal coordinate system. CMISS needs a numeric pointer 
#so we create a usernumber as below. 
coordinateSystemUserNumber = 1
coordinateSystem.CreateStart(coordinateSystemUserNumber)
#Setting dimensions because why not
coordinateSystem.dimension = 3
coordinateSystem.CreateFinish()
##Coordinate System done!

#Create a region
regionUserNumber = 1
region = CMISS.Region()
#As above
region.CreateStart(regionUserNumber, CMISS.WorldRegion)
#The create start for a region by definition requires another region as one of its parameters
region.label = "LaplaceRegion"
region.coordinateSystem = coordinateSystem
region.CreateFinish()
#Above should be pretty straight forward.
##Region done!

#Create a basis needed for interpolation of field values. Think FEM? 
basisUserNumber = 1
basis = CMISS.Basis()
basis.CreateStart(basisUserNumber)
basis.type = CMISS.BasisTypes.LAGRANGE_HERMITE_TP
basis.numberOfXi = 2
basis.interpolationXi = [
    CMISS.BasisInterpolationSpecifications.LINEAR_LAGRANGE,
    CMISS.BasisInterpolationSpecifications.LINEAR_LAGRANGE,
]
basis.quadratureNumberOfGaussXi = [2, 2]
basis.CreateFinish()

help(CMISS.BasisTypes)