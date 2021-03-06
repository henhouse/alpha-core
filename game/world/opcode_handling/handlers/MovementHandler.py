from struct import pack, unpack, error

from network.packet.PacketWriter import *
from utils.constants.OpCodes import OpCode
from utils.Logger import Logger


class MovementHandler(object):

    @staticmethod
    def handle_movement_status(world_session, socket, reader):
        movement_fmt = '<QfffffffffI'
        try:
            transport_guid, transport_x, transport_y, transport_z, transport_o, x, y, z, o, pitch, flags = \
                unpack(movement_fmt, reader.data)

            movement_data = PacketWriter.get_packet(OpCode(reader.opcode),
                                                    pack(movement_fmt,
                                                         transport_guid,
                                                         transport_x,
                                                         transport_y,
                                                         transport_z,
                                                         transport_o,
                                                         x, y, z, o,
                                                         pitch,
                                                         flags))
            socket.sendall(movement_data)

            world_session.player_mgr.transport_id = transport_guid

            world_session.player_mgr.transport_x = transport_x
            world_session.player_mgr.transport_y = transport_y
            world_session.player_mgr.transport_z = transport_z
            world_session.player_mgr.transport_orientation = transport_o

            world_session.player_mgr.location.x = x
            world_session.player_mgr.location.y = y
            world_session.player_mgr.location.z = z
            world_session.player_mgr.orientation = o

            world_session.player_mgr.pitch = pitch
            world_session.player_mgr.movement_flags = flags

        except error:
            Logger.error('Error while handling %s, skipping.' % OpCode(reader.opcode))

        return 0
