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


#ifndef SEISCOMP_GUI_OPTIONALDOUBLESPINBOX_H__
#define SEISCOMP_GUI_OPTIONALDOUBLESPINBOX_H__


#include <seiscomp/gui/qt.h>
#include <QDoubleSpinBox>


class QToolButton;


namespace Seiscomp {
namespace Gui {


class SC_GUI_API OptionalDoubleSpinBox : public QDoubleSpinBox {
	Q_OBJECT

	public:
		OptionalDoubleSpinBox(QWidget *parent = 0);

	public:
		/**
		 * @brief Returns whether the value is valid or not. A valid value
		 *        is larger than the defined minimum of the value range.
		 * @return Flag indicating validity
		 */
		bool isValid() const;

	private slots:
		void resetContent();
		void changedContent();


	private:
		QToolButton *_resetButton;
		int          _spacing;
};


}
}


#endif
