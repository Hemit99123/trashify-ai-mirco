import grpc
from concurrent import futures
from proto import main_pb2
from proto import main_pb2_grpc
import numpy as np
from sklearn.neighbors import BallTree

class TrashifyAIService(main_pb2_grpc.TrashifyServicer):
    def GetNearestCoor(self, request, context):
        # Convert repeated double coor from the request to a NumPy array
        coordinates_list = [list(coord.coor) for coord in request.coordinates]
        
        # Ensure that we have at least one coordinate
        if not coordinates_list:
            context.set_details('No coordinates provided.')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return main_pb2.NearestLocationResponse()

        coordinates = np.array(coordinates_list, dtype=float)

        # Check if coordinates array is empty
        if coordinates.shape[0] == 0:
            context.set_details('Coordinates array is empty.')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return main_pb2.NearestLocationResponse()

        # Target coordinate
        target_coordinate = np.array([list(request.query_location.coor)], dtype=float)

        # Create a BallTree instance
        try:
            tree = BallTree(coordinates, leaf_size=40)
        except ValueError as e:
            context.set_details(f'Error creating BallTree: {str(e)}')
            context.set_code(grpc.StatusCode.INTERNAL)
            return main_pb2.NearestLocationResponse()

        # Find the nearest neighbor
        distance, index = tree.query(target_coordinate, k=1)

        # Ensure indices are integers
        index = index.astype(int)

        # Get the nearest coordinate
        nearest_coordinate = coordinates[index[0][0]]

        # Construct the response object using the extracted nearest location
        nearest_location = main_pb2.CoordinateArray(coor=[nearest_coordinate[0], nearest_coordinate[1]])

        # Create the response object (defined within the proto file) and set its fields
        response = main_pb2.NearestLocationResponse(
            nearest_location=nearest_location,
        )

        # Return the response back to the client
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    main_pb2_grpc.add_TrashifyServicer_to_server(TrashifyAIService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
