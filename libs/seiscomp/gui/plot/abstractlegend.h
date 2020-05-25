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


#ifndef SEISCOMP_GUI_PLOT_ABSTRACTLEGEND_H__
#define SEISCOMP_GUI_PLOT_ABSTRACTLEGEND_H__


#include <seiscomp/gui/qt.h>
#include <QObject>
#include <QPainter>
#include <QList>


namespace Seiscomp {
namespace Gui {


class Graph;


class SC_GUI_API AbstractLegend : public QObject {
	// ----------------------------------------------------------------------
	//  X'truction
	// ----------------------------------------------------------------------
	public:
		//! C'tor
		explicit AbstractLegend(QObject *parent=0);


	// ----------------------------------------------------------------------
	//  Setup
	// ----------------------------------------------------------------------
	public:
		void setVisible(bool visible);
		bool isVisible() const { return _visible; }


	// ----------------------------------------------------------------------
	//  Render interface
	// ----------------------------------------------------------------------
	public:
		virtual void draw(QPainter &p, const QRect &plotRect,
		                  const QList<Graph*> &graphs) = 0;


	// ----------------------------------------------------------------------
	//  Render interface
	// ----------------------------------------------------------------------
	protected:
		bool _visible;
};


}
}


#endif
