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

#define SEISCOMP_TEST_MODULE TestStrings

#include <iostream>
#include <stdexcept>
#include <stdio.h>
#include <vector>
#include <limits>
#include <cstdint>

#include <seiscomp/unittest/unittests.h>

#include <seiscomp/core/strings.h>


using namespace std;
using namespace Seiscomp::Core;



vector<string> vec(const char *t1) {
	vector<string> v;
	v.push_back(t1);
	return v;
}

vector<string> vec(const char *t1, const char *t2) {
	vector<string> v;
	v.push_back(t1);
	v.push_back(t2);
	return v;
}

vector<string> vec(const char *t1, const char *t2, const char *t3) {
	vector<string> v;
	v.push_back(t1);
	v.push_back(t2);
	v.push_back(t3);
	return v;
}

vector<string> vec(const char *t1, const char *t2, const char *t3, const char *t4) {
	vector<string> v;
	v.push_back(t1);
	v.push_back(t2);
	v.push_back(t3);
	v.push_back(t4);
	return v;
}


struct TestCase {
	TestCase(const char *delimiter, bool compressOn, const char *source,
	         const vector<string> &tokens, bool trim = false)
	: delimiter(delimiter), compressOn(compressOn), source(source)
	, tokens(tokens), trim(trim) {}

	const char     *delimiter;
	bool            compressOn;
	const char     *source;
	vector<string>  tokens;
	bool            trim;
};

typedef vector<TestCase> TestData;


BOOST_AUTO_TEST_CASE(numberConversions) {
	{
		int8_t value;
		BOOST_REQUIRE(fromString(value, "10") && value == 10);
		BOOST_REQUIRE(fromString(value, "-10") && value == -10);
		BOOST_REQUIRE(fromString(value, "127") && value == 127);
		BOOST_REQUIRE(fromString(value, "-128") && value == -128);
		BOOST_REQUIRE(!fromString(value, "129"));
		BOOST_REQUIRE(!fromString(value, "-129"));
		BOOST_REQUIRE(!fromString(value, "abc"));
	}

	{
		uint8_t value;
		BOOST_REQUIRE(fromString(value, "10") && value == 10);
		BOOST_REQUIRE(!fromString(value, "-10"));
		BOOST_REQUIRE(fromString(value, "255") && value == 255);
		BOOST_REQUIRE(fromString(value, "0") && value == 0);
		BOOST_REQUIRE(!fromString(value, "256"));
		BOOST_REQUIRE(!fromString(value, "abc"));
	}

	{
		int16_t value;
		BOOST_REQUIRE(fromString(value, "10") && value == 10);
		BOOST_REQUIRE(fromString(value, "-10") && value == -10);
		BOOST_REQUIRE(fromString(value, "32767") && value == 32767);
		BOOST_REQUIRE(fromString(value, "-32768") && value == -32768);
		BOOST_REQUIRE(!fromString(value, "32768"));
		BOOST_REQUIRE(!fromString(value, "-32769"));
		BOOST_REQUIRE(!fromString(value, "abc"));
	}

	{
		uint16_t value;
		BOOST_REQUIRE(fromString(value, "10") && value == 10);
		BOOST_REQUIRE(!fromString(value, "-10"));
		BOOST_REQUIRE(fromString(value, "65535") && value == 65535);
		BOOST_REQUIRE(fromString(value, "0") && value == 0);
		BOOST_REQUIRE(!fromString(value, "65536"));
		BOOST_REQUIRE(!fromString(value, "abc"));
	}

	{
		int32_t value;
		BOOST_REQUIRE(fromString(value, "10") && value == 10);
		BOOST_REQUIRE(fromString(value, "-10") && value == -10);
		BOOST_REQUIRE(fromString(value, "2147483647") && value == 2147483647);
		BOOST_REQUIRE(fromString(value, "-2147483648") && value == -2147483648);
		BOOST_REQUIRE(!fromString(value, "2147483649"));
		BOOST_REQUIRE(!fromString(value, "-2147483649"));
		BOOST_REQUIRE(!fromString(value, "abc"));
	}

	{
		uint32_t value;
		BOOST_REQUIRE(fromString(value, "10") && value == 10);
		BOOST_REQUIRE(!fromString(value, "-10"));
		BOOST_REQUIRE(fromString(value, "4294967295") && value == 4294967295);
		BOOST_REQUIRE(fromString(value, "0") && value == 0);
		BOOST_REQUIRE(!fromString(value, "4294967296"));
		BOOST_REQUIRE(!fromString(value, "abc"));
	}

	{
		int64_t value;
		BOOST_REQUIRE(fromString(value, "10") && value == 10);
		BOOST_REQUIRE(fromString(value, "-10") && value == -10);
		BOOST_REQUIRE(fromString(value, toString(std::numeric_limits<int64_t>::max())) && value == std::numeric_limits<long>::max());
		BOOST_REQUIRE(fromString(value, toString(std::numeric_limits<int64_t>::min())) && value == std::numeric_limits<long>::min());
		BOOST_REQUIRE(!fromString(value, "abc"));
	}

	{
		// Only signed 64bit values are supported for string conversions. So
		// unsigned 64bit integers must produce ERANGE when reading values
		// larger than 2**63.
		uint64_t value;
		BOOST_REQUIRE(fromString(value, "10") && value == 10);
		BOOST_REQUIRE(!fromString(value, "-10"));
		BOOST_REQUIRE(!fromString(value, toString(std::numeric_limits<uint64_t>::max())));
		BOOST_REQUIRE(fromString(value, toString(std::numeric_limits<uint64_t>::max()/2)) && value == std::numeric_limits<unsigned long int>::max()/2);
		BOOST_REQUIRE(fromString(value, toString(std::numeric_limits<uint64_t>::min())) && value == std::numeric_limits<unsigned long int>::min());
		BOOST_REQUIRE(!fromString(value, "abc"));
	}

	{
		float value;
		BOOST_REQUIRE(fromString(value, "1.0") && fabs(value - 1.0f) < 0.000001f);
		BOOST_REQUIRE(fromString(value, "-1.0") && fabs(value + 1.0f) < 0.000001f);
		BOOST_REQUIRE(!fromString(value, "abc"));
	}

	{
		double value;
		BOOST_REQUIRE(fromString(value, "1.0") && fabs(value - 1.0) < 0.000001);
		BOOST_REQUIRE(fromString(value, "-1.0") && fabs(value + 1.0) < 0.000001);
		BOOST_REQUIRE(!fromString(value, "abc"));
	}
}


BOOST_AUTO_TEST_CASE(incompleteNumberConversions) {
	int32_t value;
	BOOST_REQUIRE(!fromString(value, "10 asd"));
	BOOST_REQUIRE(!fromString(value, "10 20"));
	BOOST_REQUIRE(!fromString(value, "1.23"));
}


BOOST_AUTO_TEST_CASE(tokenize1) {
	const char *text = "Hello, World!";
	size_t len = strlen(text), tok_len;

	const char *tok = tokenize(text, ",", len, tok_len);
	BOOST_CHECK_EQUAL(string(tok, tok_len), "Hello");

	tok = tokenize(text, ",", len, tok_len);
	BOOST_CHECK_EQUAL(string(tok,tok_len)," World!");

	text = "This is a book";
	len = strlen(text);
	int tok_count = 0;
	while ( (tok = tokenize(text, ",", len, tok_len)) != NULL ) {
		if ( tok_count == 3 ) {
			BOOST_CHECK_EQUAL(string(tok, tok_len), "book");
		}
		++tok_count;
	}

	text = "";
	len = strlen(text);
	tok = tokenize(text, ";", len,tok_len);
	BOOST_CHECK_EQUAL(string(tok,tok_len), "");

	// Test that separators collapse
	text ="A B ; C; D  ;E  ;  F";
	len = strlen(text);
	tok = tokenize(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "A", tok_len));
	tok = tokenize(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "B", tok_len));
	tok = tokenize(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "C", tok_len));
	tok = tokenize(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "D", tok_len));
	tok = tokenize(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "E", tok_len));
	tok = tokenize(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "F", tok_len));

	// Test that separators do not collapse
	text ="A B ; C; D  ;E  ;  F";
	len = strlen(text);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "A", tok_len) && tok_len == 1);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "B", tok_len) && tok_len == 1);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !tok_len);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !tok_len);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "C", tok_len) && tok_len == 1);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !tok_len);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "D", tok_len) && tok_len == 1);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !tok_len);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !tok_len);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "E", tok_len) && tok_len == 1);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !tok_len);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !tok_len);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !tok_len);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !tok_len);
	tok = tokenize2(text, " ;", len, tok_len);
	BOOST_REQUIRE(tok && !strncmp(tok, "F", tok_len) && tok_len == 1);
}


BOOST_AUTO_TEST_CASE(stringify1) {
	for ( size_t i = 1; i <= 100; ++i ) {
		string tmp;
		tmp.resize(i);
		for ( size_t j = 0; j < tmp.size(); ++j )
			tmp[j] = static_cast<char>(random() * 25 / RAND_MAX + 'A');
		string out = stringify("%s", tmp.c_str());
		BOOST_CHECK_EQUAL(tmp, out);
	}
}

BOOST_AUTO_TEST_CASE(split1) {
	TestData data;
	data.push_back(TestCase(",",  true,  ",foo,,,bar,", vec("", "foo", "bar", "")));
	data.push_back(TestCase(",",  true,  ",,foo,bar,,", vec("", "foo", "bar", "")));
	data.push_back(TestCase(" ",  true,  "foo  bar,",   vec("foo", "bar,")));
	data.push_back(TestCase(" ",  false, "foo  bar ",   vec("foo", "", "bar", "")));
	data.push_back(TestCase("oo", false, "fooobar",     vec("f", "", "", "bar")));
	data.push_back(TestCase("oo", true,  "fooooobar",   vec("f", "bar")));
	data.push_back(TestCase("ab", true,  "1a2b3",       vec("1", "2", "3")));

	vector<string> result;
	for ( TestData::const_iterator it = data.begin(); it != data.end(); ++it ) {
		split(result, it->source, it->delimiter, it->compressOn);
		BOOST_CHECK_EQUAL_COLLECTIONS(result.begin(), result.end(),
		                              it->tokens.begin(), it->tokens.end());
	}
}

BOOST_AUTO_TEST_CASE(splitExtNoUnescape) {
	typedef vector<TestCase> TestData;

	TestData data;
	data.push_back(TestCase(",",  true,  ",foo,,,bar,",               vec("", "foo", "bar", ""),          false));
	data.push_back(TestCase(",",  true,  ",,foo,bar,,",               vec("", "foo", "bar", ""),          false));
	data.push_back(TestCase(" ",  true,  "foo  bar,",                 vec("foo", "bar,"),                 false));
	data.push_back(TestCase(" ",  false, "foo  bar ",                 vec("foo", "", "bar", ""),          false));
	data.push_back(TestCase("oo", false, "fooobar",                   vec("f", "", "", "bar"),            false));
	data.push_back(TestCase("oo", true,  "fooooobar",                 vec("f", "bar"),                    false));
	data.push_back(TestCase("ab", true,  "1a2b3",                     vec("1", "2", "3"),                 false));
	data.push_back(TestCase(",",  true,  " foo , bar \r\n",           vec("foo", "bar" ),                 true));
	data.push_back(TestCase(",",  true,  " foo \\, bar, , ",          vec("foo \\, bar" ),                true));
	data.push_back(TestCase(",",  true,  " ' foo , bar ', \",bar \"", vec("' foo , bar '", "\",bar \"" ), true));
	data.push_back(TestCase(",",  true,  " \" \\\"foo\" , bar",       vec("\" \\\"foo\"", "bar" ),        true));
	data.push_back(TestCase(",",  true,  " '' \"'\" , \",',' \" ' '", vec("'' \"'\"", "\",',' \" ' '" ),  true));
	data.push_back(TestCase(" ",  true,  "foo bar",                   vec("foo", "bar" ),                 true));
	data.push_back(TestCase(" ",  true,  " foo bar ",                 vec("", "foo", "bar", "" ),         true));
	data.push_back(TestCase(" ",  true,  " foo\\ bar\r\n     a ",     vec("", "foo\\ bar\r\n", "a", "" ), false));

	vector<string> result;
	for ( TestData::const_iterator it = data.begin(); it != data.end(); ++it ) {
		splitExt(result, it->source, it->delimiter, it->compressOn, false, it->trim);
		BOOST_CHECK_EQUAL_COLLECTIONS(result.begin(), result.end(),
		                              it->tokens.begin(), it->tokens.end());
	}
}

BOOST_AUTO_TEST_CASE(splitExtUnescape) {
	typedef vector<TestCase> TestData;

	TestData data;
	data.push_back(TestCase(",",  true,  ",foo,,,bar,",               vec("", "foo", "bar", ""),        false));
	data.push_back(TestCase(",",  true,  ",,foo,bar,,",               vec("", "foo", "bar", ""),        false));
	data.push_back(TestCase(" ",  true,  "foo  bar,",                 vec("foo", "bar,"),               false));
	data.push_back(TestCase(" ",  false, "foo  bar ",                 vec("foo", "", "bar", ""),        false));
	data.push_back(TestCase("oo", false, "fooobar",                   vec("f", "", "", "bar"),          false));
	data.push_back(TestCase("oo", true,  "fooooobar",                 vec("f", "bar"),                  false));
	data.push_back(TestCase("ab", true,  "1a2b3",                     vec("1", "2", "3"),               false));
	data.push_back(TestCase(",",  true,  " foo , bar \r\n",           vec("foo", "bar"),                true));
	data.push_back(TestCase(",",  true,  " foo \\, bar, , ",          vec("foo , bar"),                 true));
	data.push_back(TestCase(",",  true,  " ' foo , bar ', \",bar \"", vec(" foo , bar ", ",bar "),      true));
	data.push_back(TestCase(",",  true,  " \" \\t \\\"foo\" , bar",   vec(" \\t \"foo", "bar"),         true));
	data.push_back(TestCase(",",  true,  " \\\\\\ , \\ \\t'\\\\\\'\\ \\t'", vec("\\ ", " \\t\\'\\ \\t"),  true));
	data.push_back(TestCase(",",  true,  " '' \"'\" , \",',' \" ' '", vec("'", ",','   "),              true));
	data.push_back(TestCase(" ",  true,  "foo bar",                   vec("foo", "bar"),                true));
	data.push_back(TestCase(" ",  true,  " foo bar ",                 vec("", "foo", "bar", ""),        true));
	data.push_back(TestCase(" ",  true,  " foo\\ bar\r\n   \\\\   ",  vec("", "foo bar\r\n", "\\", ""), false));
	data.push_back(TestCase(" ",  true,  "' foo\\ bar' test",         vec(" foo\\ bar", "test"),        true));
	data.push_back(TestCase(",",  true,  "\\",                        vec("\\"),                        true));
	data.push_back(TestCase(",",  true,  "\\ ",                       vec(" "),                         true));
	data.push_back(TestCase(",",  true,  " \\",                       vec("\\"),                        true));
	data.push_back(TestCase(",",  true,  "\\ ",                       vec(" "),                         false));
	data.push_back(TestCase(",",  true,  " \\",                       vec(" \\"),                       false));
	data.push_back(TestCase(",",  true,  "\\\"\\t\\\\\\ \\,\\\\\\ \\\\\\t",   vec("\"\\t\\ ,\\ \\\\t"),         true));
	data.push_back(TestCase(",",  true,  "'\\\"\\t\\\\\\ \\,\\\\\\ \\\\\\t'", vec("\\\"\\t\\\\ \\,\\\\ \\\\t"), true));

	vector<string> result;
	for ( TestData::const_iterator it = data.begin(); it != data.end(); ++it ) {
		splitExt(result, it->source, it->delimiter, it->compressOn, true, it->trim);
		BOOST_CHECK_EQUAL_COLLECTIONS(result.begin(), result.end(),
		                              it->tokens.begin(), it->tokens.end());
	}
}
