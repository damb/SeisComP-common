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


#ifndef SEISCOMP_CORE_RTTI_H
#define SEISCOMP_CORE_RTTI_H


#include <seiscomp/core.h>
#include <string>


namespace Seiscomp {
namespace Core {

// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
/**	\brief A RTTI (Runtime Type Information) class

	This class implements an RTTI object returned by the
	RTTI interface below (DECLARE_RTTI).
	It supports retrieving a classname, the parent type information
	and comparing two types for equality or collating order.
	Drawback: No multiple inheritance supported!

	To implement it into your own classes, use the supported RTTI
	macros.

	\code
	class MyClass {
		DECLARE_RTTI;
		...
		public:
			MyClass();
		...
	};
	\endcode

	To implement the RTTI interface, another macro is to be used. There are
	two versions. One version to implement the RTTI interface for the root type
	and another version for derived types.
	\code
	IMPLEMENT_ROOT_RTTI(MyClass, MyClassNameWithRespectToMyRTTI);
	\endcode

	and

	\code
	IMPLEMENT_RTTI(MyDerivedClass, MyDerivedClassNameWithRespectToMyRTTI, MyClass);
	\endcode
 */
class SC_SYSTEM_CORE_API RTTI {
	// ----------------------------------------------------------------------
	//  Xstruction
	// ----------------------------------------------------------------------
	public:
		//! Constructor
		RTTI(const char* classname, const RTTI* parent = nullptr);


	// ----------------------------------------------------------------------
	//  Operators
	// ----------------------------------------------------------------------
	public:
		//! Checks two types for equality
		bool operator==(const RTTI& other) const;
		bool operator!=(const RTTI& other) const;


	// ----------------------------------------------------------------------
	//  Public interface
	// ----------------------------------------------------------------------
	public:
		const RTTI* parent() const;
		const char* className() const;

		//! Returns whether other is derived from *this or not.
		//! If both types are equal, false is returned.
		bool before(const RTTI& other) const;

		//! Returns true when *this is derived from or equal to other
		bool isTypeOf(const RTTI& other) const;


	// ----------------------------------------------------------------------
	//  Implementation
	// ----------------------------------------------------------------------
	private:
		std::string _classname;
		const RTTI* _parent;
};
// <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<





// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#define DECLARE_BASE_RTTI \
	public: \
		static const char* ClassName(); \
		static const Seiscomp::Core::RTTI& TypeInfo(); \
		\
		virtual const char* className() const; \
		virtual const Seiscomp::Core::RTTI& typeInfo() const


#define DECLARE_RTTI \
	public: \
		static const char* ClassName(); \
		static const Seiscomp::Core::RTTI& TypeInfo(); \
		\
		virtual const char* className() const override; \
		virtual const Seiscomp::Core::RTTI& typeInfo() const override


#define IMPLEMENT_ROOT_RTTI(CLASS, CLASSNAME) \
	const Seiscomp::Core::RTTI& CLASS::TypeInfo() { \
		static Seiscomp::Core::RTTI classRTTI(CLASSNAME); \
		return classRTTI; \
	}


#define IMPLEMENT_RTTI(CLASS, CLASSNAME, BASECLASS) \
	const Seiscomp::Core::RTTI& CLASS::TypeInfo() { \
		static Seiscomp::Core::RTTI classRTTI(CLASSNAME, &BASECLASS::TypeInfo()); \
		return classRTTI; \
	}



#define IMPLEMENT_TEMPLATE_RTTI(CLASS, CLASSNAME, BASECLASS) \
	template <> \
	const Seiscomp::Core::RTTI& CLASS::TypeInfo() { \
		static Seiscomp::Core::RTTI classRTTI(CLASSNAME, &BASECLASS::TypeInfo()); \
		return classRTTI; \
	}


#define IMPLEMENT_RTTI_METHODS(CLASS) \
	const char* CLASS::ClassName() { \
		return TypeInfo().className(); \
	} \
	\
	const char* CLASS::className() const { \
		return TypeInfo().className(); \
	} \
	\
	const Seiscomp::Core::RTTI& CLASS::typeInfo() const { \
		return TypeInfo(); \
	}


#define IMPLEMENT_TEMPLATE_RTTI_METHODS(CLASS, CLASSNAME) \
	template <typename T> \
	inline const char* CLASS<T>::ClassName() { \
		return TypeInfo().className(); \
	} \
	\
	template <typename T> \
	inline const Seiscomp::Core::RTTI& CLASS<T>::TypeInfo() { \
		static Seiscomp::Core::RTTI classRTTI(CLASSNAME); \
		return classRTTI; \
	} \
	template <typename T> \
	inline const char* CLASS<T>::className() const { \
		return TypeInfo().className(); \
	} \
	\
	template <typename T> \
	inline const Seiscomp::Core::RTTI& CLASS<T>::typeInfo() const { \
		return TypeInfo(); \
	}
// <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<





// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
}
}


#endif
