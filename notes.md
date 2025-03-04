we need to take a collection of points in 3d space, turn them into triangles and project them to the screen.

Verticies (set of 3 floats to represent a coordinate)
Triangle (Set of 3 verticies)
Mesh (collection of any number of triangles)

To start with we can initialize a cube's points manualy.
each face will have 2 triangles, lets define them clockwise.

probably want to normalize the screen space where 0,0 is in the middle

try your best to understand the projection maths but if you cant thats ok.
