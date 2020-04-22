/***************************************************************************
 * Copyright (C) gempa GmbH                                                *
 * All rights reserved.                                                    *
 * Contact: gempa GmbH (seiscomp-dev@gempa.de)                             *
 *                                                                         *
 * GNU Affero General Public License Usage                                 *
 * This file may be used under the terms of the GNU Affero                 *
 * Public License version 3.0 as published by the Free Software Foundation *
 * and appearing in the file LICENSE included in the packaging of this     *
 * file. Please review the following information to ensure the GNU Affero  *
 * Public License version 3.0 requirements will be met:                    *
 * https://www.gnu.org/licenses/agpl-3.0.html.                             *
 *                                                                         *
 * Other Usage                                                             *
 * Alternatively, this file may be used in accordance with the terms and   *
 * conditions contained in a signed written agreement between you and      *
 * gempa GmbH.                                                             *
 ***************************************************************************/


#ifndef SEISCOMP_WIRED_SESSION_H
#define SEISCOMP_WIRED_SESSION_H


#include <seiscomp/wired/devices/socket.h>
#include <seiscomp/core/list.h>


namespace Seiscomp {
namespace Wired {


class Reactor;
class Server;


DEFINE_SMARTPOINTER(Session);

class SC_SYSTEM_CORE_API Session : public Core::BaseObject,
                                   public Core::Generic::IntrusiveListItem<SessionPtr> {
	// ----------------------------------------------------------------------
	//  X'truction
	// ----------------------------------------------------------------------
	protected:
		//! Protected c'tor
		Session(Device *dev);


	// ----------------------------------------------------------------------
	//  Public interface
	// ----------------------------------------------------------------------
	public:
		virtual ~Session();

		void setDevice(Device *dev);
		Device *device() const;

		Reactor *parent() const { return _parent; }

		//! Update the session state.
		virtual void update() = 0;

		//! Close the session and terminate the connection.
		virtual void close();

		void setTag(bool t) { _tagged = t; }
		bool isTagged() const { return _tagged; }


	// ----------------------------------------------------------------------
	//  Protected members
	// ----------------------------------------------------------------------
	protected:
		DevicePtr    _device;
		Reactor     *_parent;


	// ----------------------------------------------------------------------
	//  Private members
	// ----------------------------------------------------------------------
	private:
		bool         _tagged;


	// ----------------------------------------------------------------------
	//  Friends
	// ----------------------------------------------------------------------
	friend class Reactor;
	friend class Server;
};


}
}


#endif
